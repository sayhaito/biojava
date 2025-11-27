#!/usr/bin/env python3
"""
A8 Documentation Assembly - BioJava
Assembles comprehensive Markdown documentation from all analysis artifacts
"""
import os
import json
from pathlib import Path

def assemble_module_documentation(module_name):
    """Assemble complete documentation for a module"""
    base_dir = '/home/user/biojava/analysis'

    # Load artifacts
    module_map_file = os.path.join(base_dir, 'A2_modules', f'{module_name}_module_map.json')
    classes_file = os.path.join(base_dir, 'A3_classes', f'{module_name}_classes.json')
    methods_file = os.path.join(base_dir, 'A4_methods', f'{module_name}_methods.json')
    flows_file = os.path.join(base_dir, 'A7_business_flows', f'{module_name}_business_flows.json')

    doc_lines = []

    # Header
    doc_lines.append(f"# {module_name} — Technical Documentation")
    doc_lines.append("")
    doc_lines.append("---")
    doc_lines.append("")

    # Module Overview
    if os.path.exists(module_map_file):
        with open(module_map_file, 'r') as f:
            module_map = json.load(f)

        doc_lines.append("## Module Overview")
        doc_lines.append("")
        doc_lines.append(f"**Module:** `{module_map['module']}`  ")
        doc_lines.append(f"**Total Classes:** {module_map['total_classes']}  ")
        doc_lines.append(f"**Packages:** {len(module_map['packages'])}")
        doc_lines.append("")

        doc_lines.append("### Packages")
        doc_lines.append("")
        for pkg in module_map['packages'][:15]:
            doc_lines.append(f"- `{pkg}`")
        doc_lines.append("")

        doc_lines.append("### Dependencies")
        doc_lines.append("")
        doc_lines.append("**External:**")
        for dep in module_map['dependencies']['external'][:10]:
            doc_lines.append(f"- {dep}")
        doc_lines.append("")

        if module_map['dependencies']['internal']:
            doc_lines.append("**Internal:**")
            for dep in module_map['dependencies']['internal'][:5]:
                doc_lines.append(f"- {dep}")
            doc_lines.append("")

        doc_lines.append("---")
        doc_lines.append("")

    # Business Flows
    if os.path.exists(flows_file):
        with open(flows_file, 'r') as f:
            flows = json.load(f)

        doc_lines.append("## Business Process Flows")
        doc_lines.append("")

        for flow in flows[:5]:
            doc_lines.append(f"### {flow['feature']}")
            doc_lines.append("")
            doc_lines.append(f"**Actor:** {flow['actor']}  ")
            doc_lines.append(f"**Summary:** {flow['summary']}")
            doc_lines.append("")

            doc_lines.append("**Steps:**")
            for i, step in enumerate(flow['steps'], 1):
                doc_lines.append(f"{i}. {step}")
            doc_lines.append("")

            # Reference to activity diagram
            activity_file = f"{module_name}_{flow['feature']}_activity.puml"
            doc_lines.append(f"![Activity Diagram](../A7_business_flows/{activity_file})")
            doc_lines.append("")

        doc_lines.append("---")
        doc_lines.append("")

    # Class Structures
    if os.path.exists(classes_file):
        with open(classes_file, 'r') as f:
            classes = json.load(f)

        doc_lines.append("## Key Classes")
        doc_lines.append("")

        for cls in classes[:8]:
            doc_lines.append(f"### {cls['class_name']}")
            doc_lines.append("")
            doc_lines.append(f"**Package:** `{cls['package']}`  ")
            doc_lines.append(f"**Type:** {cls['type']}")
            doc_lines.append("")

            if cls.get('extends'):
                doc_lines.append(f"**Extends:** `{cls['extends']}`  ")

            if cls.get('implements'):
                doc_lines.append(f"**Implements:** {', '.join([f'`{i}`' for i in cls['implements']])}  ")

            doc_lines.append("")

            # Fields
            if cls.get('fields'):
                doc_lines.append("**Fields:**")
                doc_lines.append("")
                doc_lines.append("| Visibility | Type | Name |")
                doc_lines.append("|------------|------|------|")
                for field in cls['fields'][:10]:
                    doc_lines.append(f"| {field['visibility']} | `{field['type']}` | {field['name']} |")
                doc_lines.append("")

            # Methods
            if cls.get('methods'):
                doc_lines.append("**Methods:**")
                doc_lines.append("")
                for method in cls['methods'][:10]:
                    params = ', '.join(method.get('params', []))
                    doc_lines.append(f"- `{method['return_type']} {method['name']}({params})`")
                doc_lines.append("")

        # Reference to class diagram
        class_diagram_file = f"{module_name}_class_diagram.puml"
        doc_lines.append(f"### Class Diagram")
        doc_lines.append("")
        doc_lines.append(f"![Class Diagram](../A6_uml/{class_diagram_file})")
        doc_lines.append("")

        doc_lines.append("---")
        doc_lines.append("")

    # Method Logic
    if os.path.exists(methods_file):
        with open(methods_file, 'r') as f:
            methods = json.load(f)

        doc_lines.append("## Method Logic Flows")
        doc_lines.append("")

        for method in methods[:5]:
            doc_lines.append(f"### {method['class']}.{method['method']}()")
            doc_lines.append("")

            # Steps
            if method.get('steps'):
                doc_lines.append("**Execution Steps:**")
                doc_lines.append("")
                for i, step in enumerate(method['steps'], 1):
                    doc_lines.append(f"{i}. `{step}`")
                doc_lines.append("")

            # Branches
            if method.get('branches'):
                doc_lines.append("**Conditional Logic:**")
                doc_lines.append("")
                for branch in method['branches']:
                    doc_lines.append(f"- **Condition:** `{branch['condition']}`")
                doc_lines.append("")

            # Loops
            if method.get('loops'):
                doc_lines.append("**Loops:**")
                doc_lines.append("")
                for loop in method['loops']:
                    doc_lines.append(f"- **Type:** {loop['type']}")
                doc_lines.append("")

            # External calls
            if method.get('external_calls'):
                doc_lines.append("**External Calls:**")
                doc_lines.append("")
                for call in method['external_calls'][:10]:
                    doc_lines.append(f"- `{call}`")
                doc_lines.append("")

            # Exceptions
            if method.get('exceptions'):
                doc_lines.append("**Exceptions:** {0}".format(', '.join([f'`{e}`' for e in method['exceptions']])))
                doc_lines.append("")

        # Reference to sequence diagram
        sequence_diagram_file = f"{module_name}_sequence_diagram.puml"
        if os.path.exists(os.path.join(base_dir, 'A6_uml', sequence_diagram_file)):
            doc_lines.append(f"### Sequence Diagram")
            doc_lines.append("")
            doc_lines.append(f"![Sequence Diagram](../A6_uml/{sequence_diagram_file})")
            doc_lines.append("")

        doc_lines.append("---")
        doc_lines.append("")

    return '\n'.join(doc_lines)

def main():
    """Main entry point"""
    base_dir = '/home/user/biojava/analysis'
    output_dir = os.path.join(base_dir, 'A8_documentation')

    os.makedirs(output_dir, exist_ok=True)

    # Get all modules
    module_dir = os.path.join(base_dir, 'A2_modules')
    module_files = [f for f in os.listdir(module_dir) if f.endswith('_module_map.json')]

    modules = [f.replace('_module_map.json', '') for f in module_files]

    # Generate master documentation
    master_doc = []
    master_doc.append("# BioJava — Complete Code Analysis Documentation")
    master_doc.append("")
    master_doc.append("**Project:** BioJava v7.2.4-SNAPSHOT  ")
    master_doc.append("**Analysis Date:** 2025-11-27  ")
    master_doc.append("**Analysis Framework:** Expert Java Engineer Role (A2-A8)")
    master_doc.append("")
    master_doc.append("---")
    master_doc.append("")

    master_doc.append("## Table of Contents")
    master_doc.append("")
    for module in modules:
        master_doc.append(f"- [{module}]({module}_documentation.md)")
    master_doc.append("")
    master_doc.append("---")
    master_doc.append("")

    # Project summary
    summary_file = os.path.join(base_dir, 'A2_modules', 'project_summary.json')
    if os.path.exists(summary_file):
        with open(summary_file, 'r') as f:
            summary = json.load(f)

        master_doc.append("## Project Summary")
        master_doc.append("")
        master_doc.append(f"- **Total Modules:** {summary['total_modules']}")
        master_doc.append(f"- **Total Classes:** {summary['total_classes']}")
        master_doc.append("")

    # Write master document
    master_file = os.path.join(output_dir, 'README.md')
    with open(master_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(master_doc))
    print(f"✓ Master documentation: {master_file}")

    # Generate individual module documentation
    for module in modules:
        print(f"Assembling documentation for: {module}")

        doc_content = assemble_module_documentation(module)

        output_file = os.path.join(output_dir, f"{module}_documentation.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(doc_content)

        print(f"  ✓ Saved: {output_file}")

    # Final summary
    summary = {
        "project": "BioJava",
        "documentation_assembled": True,
        "modules_documented": len(modules),
        "analysis_level": "A8_DOCUMENTATION_ASSEMBLY",
        "status": "COMPLETE"
    }

    summary_file = os.path.join(output_dir, "documentation_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print(f"\n✓ Total modules documented: {len(modules)}")
    print(f"✓ Summary saved: {summary_file}")

if __name__ == '__main__':
    main()
