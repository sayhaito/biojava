#!/usr/bin/env python3
"""
A3 Class Structure Analysis Script - BioJava
Analyzes class structures and generates class_structure.json
"""
import os
import json
import re
from pathlib import Path

def extract_imports(content):
    """Extract import statements"""
    imports = []
    for match in re.finditer(r'import\s+(.*?);', content):
        imports.append(match.group(1).strip())
    return imports

def extract_class_info(content):
    """Extract class name, type, extends, implements"""
    # Remove comments
    content_clean = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content_clean = re.sub(r'//.*?\n', '\n', content_clean)

    # Find class/interface/enum declaration
    class_pattern = r'\b(public\s+)?(abstract\s+)?(class|interface|enum)\s+(\w+)(\s+extends\s+([\w<>,\s]+))?(\s+implements\s+([\w<>,\s]+))?'
    match = re.search(class_pattern, content_clean)

    if not match:
        return None, None, None, None

    class_type = match.group(3)  # class, interface, or enum
    class_name = match.group(4)
    extends = match.group(6).strip() if match.group(6) else None
    implements = match.group(8).strip() if match.group(8) else None

    # Handle abstract
    if match.group(2):
        class_type = 'abstract'

    # Parse implements
    implements_list = []
    if implements:
        implements_list = [i.strip() for i in implements.split(',')]

    return class_name, class_type, extends, implements_list

def extract_fields(content):
    """Extract field declarations"""
    fields = []

    # Remove comments
    content_clean = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content_clean = re.sub(r'//.*?\n', '\n', content_clean)

    # Find fields (simplified pattern)
    field_pattern = r'\b(private|protected|public|static|final)\s+(?:static\s+)?(?:final\s+)?([\w<>\[\]]+)\s+(\w+)\s*[=;]'

    for match in re.finditer(field_pattern, content_clean):
        visibility = match.group(1)
        field_type = match.group(2)
        field_name = match.group(3)

        fields.append({
            "name": field_name,
            "type": field_type,
            "visibility": visibility
        })

    return fields

def extract_methods(content):
    """Extract method declarations"""
    methods = []

    # Remove comments
    content_clean = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content_clean = re.sub(r'//.*?\n', '\n', content_clean)

    # Method pattern
    method_pattern = r'\b(public|private|protected)\s+(?:static\s+)?(?:final\s+)?([\w<>\[\]]+)\s+(\w+)\s*\((.*?)\)\s*(?:throws\s+[\w,\s]+)?\s*\{'

    for match in re.finditer(method_pattern, content_clean):
        visibility = match.group(1)
        return_type = match.group(2)
        method_name = match.group(3)
        params_str = match.group(4).strip()

        # Parse parameters
        params = []
        if params_str:
            for param in params_str.split(','):
                param = param.strip()
                if param:
                    params.append(param)

        methods.append({
            "name": method_name,
            "params": params,
            "return_type": return_type,
            "visibility": visibility
        })

    return methods

def extract_annotations(content):
    """Extract class-level annotations"""
    annotations = []
    for match in re.finditer(r'@(\w+)(?:\([^)]*\))?', content):
        annotations.append(f"@{match.group(1)}")
    return list(set(annotations))[:10]  # Limit to 10 unique

def find_references(content, imports):
    """Find internal and external references"""
    internal_refs = []
    external_refs = []

    for imp in imports:
        if 'org.biojava' in imp:
            class_name = imp.split('.')[-1]
            internal_refs.append(class_name)
        else:
            # External libraries
            if 'java.lang' not in imp and 'java.util' not in imp:
                external_refs.append(imp)

    return list(set(internal_refs)), list(set(external_refs))

def analyze_class(file_path, package):
    """Analyze a single Java class"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        class_name, class_type, extends, implements_list = extract_class_info(content)

        if not class_name:
            return None

        imports = extract_imports(content)
        fields = extract_fields(content)
        methods = extract_methods(content)
        annotations = extract_annotations(content)
        internal_refs, external_refs = find_references(content, imports)

        class_structure = {
            "class_name": class_name,
            "package": package,
            "type": class_type,
            "extends": extends,
            "implements": implements_list,
            "fields": fields[:20],  # Limit to 20
            "methods": methods[:30],  # Limit to 30
            "annotations": annotations,
            "internal_references": internal_refs[:20],
            "external_references": external_refs[:20],
            "next_step": "continue"
        }

        return class_structure

    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None

def select_important_classes(module_map):
    """Select important classes to analyze from a module"""
    classes = module_map.get('classes', [])

    # Heuristics for importance:
    # 1. Classes with common names (Service, Manager, Parser, Builder, Factory)
    # 2. Public interfaces
    # 3. Classes in root packages

    important = []
    keywords = ['Service', 'Manager', 'Parser', 'Reader', 'Writer', 'Builder',
                'Factory', 'Loader', 'Sequence', 'Structure', 'Alignment', 'Protein']

    for cls in classes:
        name = cls['name']
        # Check for important keywords
        if any(kw in name for kw in keywords):
            important.append(cls)
        # Interfaces are important
        elif cls['type'] == 'interface':
            important.append(cls)

    # If we have too many, limit to 15 per module
    if len(important) > 15:
        important = important[:15]

    # If we have too few, add some random ones
    if len(important) < 5 and len(classes) > 0:
        for cls in classes:
            if cls not in important:
                important.append(cls)
                if len(important) >= 5:
                    break

    return important

def main():
    """Main entry point"""
    biojava_root = '/home/user/biojava'
    module_dir = '/home/user/biojava/analysis/A2_modules'
    output_dir = '/home/user/biojava/analysis/A3_classes'

    os.makedirs(output_dir, exist_ok=True)

    # Read all module maps
    module_files = [f for f in os.listdir(module_dir) if f.endswith('_module_map.json')]

    total_analyzed = 0

    for module_file in module_files:
        with open(os.path.join(module_dir, module_file), 'r') as f:
            module_map = json.load(f)

        module_name = module_map['module']
        print(f"\nAnalyzing classes in: {module_name}")

        # Select important classes
        important_classes = select_important_classes(module_map)

        module_classes = []

        for cls in important_classes:
            file_path = os.path.join(biojava_root, module_name, cls['path'])

            if os.path.exists(file_path):
                class_struct = analyze_class(file_path, cls['package'])

                if class_struct:
                    module_classes.append(class_struct)
                    print(f"  ✓ {class_struct['class_name']}")
                    total_analyzed += 1

        # Save module class structures
        if module_classes:
            output_file = os.path.join(output_dir, f"{module_name}_classes.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(module_classes, f, indent=2)

    # Summary
    summary = {
        "project": "BioJava",
        "total_classes_analyzed": total_analyzed,
        "analysis_level": "A3_CLASS_STRUCTURE",
        "next_step": "A4_METHOD_LOGIC"
    }

    summary_file = os.path.join(output_dir, "class_analysis_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print(f"\n✓ Total classes analyzed: {total_analyzed}")
    print(f"✓ Summary saved: {summary_file}")

if __name__ == '__main__':
    main()
