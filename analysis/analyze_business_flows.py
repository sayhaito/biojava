#!/usr/bin/env python3
"""
A7 Business Process Flow Analyzer - BioJava
Analyzes high-level business/feature flows and generates activity diagrams
"""
import os
import json

def analyze_feature_flow(class_struct, module_name):
    """Analyze feature flow from class structure"""
    class_name = class_struct['class_name']
    package = class_struct['package']
    methods = class_struct.get('methods', [])

    # Infer feature based on class name and methods
    feature_name = class_name

    # Determine actor
    actor = "User"
    if 'Parser' in class_name or 'Reader' in class_name:
        actor = "System"
    elif 'Service' in class_name:
        actor = "Application"

    # Build summary
    summary_parts = []
    if 'Parser' in class_name:
        summary_parts.append("parses input data")
    if 'Reader' in class_name:
        summary_parts.append("reads data from source")
    if 'Writer' in class_name:
        summary_parts.append("writes data to destination")
    if 'Builder' in class_name:
        summary_parts.append("constructs objects")
    if 'Sequence' in class_name:
        summary_parts.append("manipulates biological sequences")
    if 'Structure' in class_name:
        summary_parts.append("processes molecular structures")

    summary = f"{actor} uses {class_name} to {' and '.join(summary_parts) if summary_parts else 'perform operations'}"

    # Extract steps from methods
    steps = []
    for method in methods[:10]:
        method_name = method['name']

        # Convert method names to business steps
        if method_name.startswith('get'):
            steps.append(f"Retrieve {method_name[3:]}")
        elif method_name.startswith('set'):
            steps.append(f"Set {method_name[3:]}")
        elif method_name.startswith('parse'):
            steps.append(f"Parse {method_name[5:]}")
        elif method_name.startswith('read'):
            steps.append(f"Read {method_name[4:]}")
        elif method_name.startswith('write'):
            steps.append(f"Write {method_name[5:]}")
        elif method_name.startswith('create') or method_name.startswith('build'):
            steps.append(f"Create {method_name[6:]}")
        elif method_name.startswith('process'):
            steps.append(f"Process {method_name[7:]}")
        else:
            steps.append(f"Execute {method_name}")

    # Limit steps
    steps = steps[:8]

    business_flow = {
        "feature": feature_name,
        "module": module_name,
        "actor": actor,
        "summary": summary,
        "steps": steps,
        "next_step": "continue"
    }

    return business_flow

def generate_activity_diagram(business_flow):
    """Generate PlantUML activity diagram"""
    lines = ['@startuml', f'title {business_flow["feature"]} - Activity Flow', '']

    lines.append('start')

    for step in business_flow.get('steps', []):
        lines.append(f':{step};')

    lines.append('stop')
    lines.append('')
    lines.append('@enduml')

    return '\n'.join(lines)

def main():
    """Main entry point"""
    class_dir = '/home/user/biojava/analysis/A3_classes'
    output_dir = '/home/user/biojava/analysis/A7_business_flows'

    os.makedirs(output_dir, exist_ok=True)

    # Read all class analysis files
    class_files = [f for f in os.listdir(class_dir) if f.endswith('_classes.json')]

    total_flows = 0

    for class_file in class_files:
        module_name = class_file.replace('_classes.json', '')

        with open(os.path.join(class_dir, class_file), 'r') as f:
            class_structs = json.load(f)

        print(f"\nAnalyzing business flows for: {module_name}")

        module_flows = []
        module_diagrams = []

        for class_struct in class_structs[:5]:  # Limit to 5 per module
            business_flow = analyze_feature_flow(class_struct, module_name)

            if business_flow['steps']:  # Only include if there are steps
                module_flows.append(business_flow)

                # Generate activity diagram
                activity_diagram = generate_activity_diagram(business_flow)
                module_diagrams.append({
                    "feature": business_flow['feature'],
                    "diagram": activity_diagram
                })

                print(f"  ✓ {business_flow['feature']}")
                total_flows += 1

        # Save module business flows
        if module_flows:
            output_file = os.path.join(output_dir, f"{module_name}_business_flows.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(module_flows, f, indent=2)

        # Save activity diagrams
        if module_diagrams:
            for diagram in module_diagrams:
                diagram_file = os.path.join(output_dir,
                                             f"{module_name}_{diagram['feature']}_activity.puml")
                with open(diagram_file, 'w', encoding='utf-8') as f:
                    f.write(diagram['diagram'])

    # Summary
    summary = {
        "project": "BioJava",
        "total_business_flows": total_flows,
        "analysis_level": "A7_BUSINESS_FLOWS",
        "next_step": "A8_DOCUMENTATION_ASSEMBLY"
    }

    summary_file = os.path.join(output_dir, "business_flow_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print(f"\n✓ Total business flows analyzed: {total_flows}")
    print(f"✓ Summary saved: {summary_file}")

if __name__ == '__main__':
    main()
