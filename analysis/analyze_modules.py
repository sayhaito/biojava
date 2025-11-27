#!/usr/bin/env python3
"""
A2 Module Analysis Script - BioJava
Analyzes all modules and generates module_map.json for each
"""
import os
import json
import re
from pathlib import Path
from collections import defaultdict

def extract_package_from_file(file_path):
    """Extract package declaration from Java file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if line.strip().startswith('package '):
                    return line.strip().replace('package ', '').replace(';', '').strip()
    except:
        pass
    return "unknown"

def get_class_type(file_path):
    """Determine if file contains class, interface, enum, or abstract class"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Remove comments
            content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
            content = re.sub(r'//.*?\n', '\n', content)

            if re.search(r'\bpublic\s+enum\s+', content):
                return 'enum'
            elif re.search(r'\bpublic\s+interface\s+', content):
                return 'interface'
            elif re.search(r'\bpublic\s+abstract\s+class\s+', content):
                return 'abstract'
            elif re.search(r'\bpublic\s+class\s+', content):
                return 'class'
            elif re.search(r'\bclass\s+', content):
                return 'class'
            elif re.search(r'\binterface\s+', content):
                return 'interface'
    except:
        pass
    return 'class'

def extract_dependencies(pom_path):
    """Extract dependencies from pom.xml"""
    external_deps = []
    internal_deps = []

    try:
        with open(pom_path, 'r', encoding='utf-8') as f:
            content = f.read()

            # Extract groupId and artifactId
            deps = re.findall(r'<dependency>.*?</dependency>', content, re.DOTALL)
            for dep in deps:
                group_match = re.search(r'<groupId>(.*?)</groupId>', dep)
                artifact_match = re.search(r'<artifactId>(.*?)</artifactId>', dep)

                if group_match and artifact_match:
                    group_id = group_match.group(1).strip()
                    artifact_id = artifact_match.group(1).strip()

                    if 'biojava' in artifact_id:
                        internal_deps.append(f"{group_id}.{artifact_id}")
                    else:
                        external_deps.append(f"{group_id}")

    except Exception as e:
        pass

    # Remove duplicates and sort
    external_deps = sorted(list(set(external_deps)))
    internal_deps = sorted(list(set(internal_deps)))

    return external_deps, internal_deps

def analyze_module(module_path, module_name):
    """Analyze a single BioJava module"""
    print(f"Analyzing module: {module_name}")

    src_path = os.path.join(module_path, 'src/main/java')
    pom_path = os.path.join(module_path, 'pom.xml')

    if not os.path.exists(src_path):
        return None

    # Collect classes
    classes = []
    packages = set()

    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, module_path)

                class_name = file.replace('.java', '')
                package = extract_package_from_file(file_path)
                class_type = get_class_type(file_path)

                if package != "unknown" and package != "demo":
                    packages.add(package)
                    classes.append({
                        "name": class_name,
                        "path": rel_path,
                        "type": class_type,
                        "package": package
                    })

    # Extract dependencies
    external_deps, internal_deps = extract_dependencies(pom_path)

    # Build module map
    module_map = {
        "module": module_name,
        "packages": sorted(list(packages)),
        "total_classes": len(classes),
        "classes": classes,
        "dependencies": {
            "external": external_deps,
            "internal": internal_deps
        },
        "next_step": "continue"
    }

    return module_map

def main():
    """Main entry point"""
    biojava_root = '/home/user/biojava'
    output_dir = '/home/user/biojava/analysis/A2_modules'

    modules = [
        'biojava-core',
        'biojava-alignment',
        'biojava-structure',
        'biojava-structure-gui',
        'biojava-genome',
        'biojava-modfinder',
        'biojava-ws',
        'biojava-protein-disorder',
        'biojava-aa-prop',
        'biojava-survival',
        'biojava-ontology',
        'biojava-protein-comparison-tool',
        'biojava-integrationtest'
    ]

    os.makedirs(output_dir, exist_ok=True)

    all_modules = []

    for module_name in modules:
        module_path = os.path.join(biojava_root, module_name)

        if os.path.exists(module_path):
            module_map = analyze_module(module_path, module_name)

            if module_map:
                all_modules.append(module_map)

                # Save individual module map
                output_file = os.path.join(output_dir, f"{module_name}_module_map.json")
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(module_map, f, indent=2)
                print(f"  ✓ Saved: {output_file}")

    # Save summary
    summary = {
        "project": "BioJava",
        "total_modules": len(all_modules),
        "modules": [m["module"] for m in all_modules],
        "total_classes": sum(m["total_classes"] for m in all_modules),
        "analysis_level": "A2_MODULE_ANALYSIS",
        "next_step": "A3_CLASS_STRUCTURE"
    }

    summary_file = os.path.join(output_dir, "project_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    print(f"\n✓ Summary saved: {summary_file}")

if __name__ == '__main__':
    main()
