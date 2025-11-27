#!/usr/bin/env python3
"""
A6 UML Generator - BioJava
Generates PlantUML diagrams (class + sequence) from analysis artifacts
"""
import os
import json

def generate_class_diagram(class_structs, module_name):
    """Generate PlantUML class diagram"""
    lines = ['@startuml', f'title {module_name} - Class Diagram', '']

    for cls in class_structs[:10]:  # Limit to 10 classes per diagram
        class_name = cls['class_name']
        class_type = cls['type']

        if class_type == 'interface':
            lines.append(f'interface {class_name} {{')
        elif class_type == 'abstract':
            lines.append(f'abstract class {class_name} {{')
        elif class_type == 'enum':
            lines.append(f'enum {class_name} {{')
        else:
            lines.append(f'class {class_name} {{')

        # Add fields
        for field in cls.get('fields', [])[:5]:
            visibility = field['visibility']
            symbol = '+' if visibility == 'public' else ('-' if visibility == 'private' else '#')
            lines.append(f'  {symbol} {field["name"]}: {field["type"]}')

        # Add methods
        for method in cls.get('methods', [])[:8]:
            visibility = method['visibility']
            symbol = '+' if visibility == 'public' else ('-' if visibility == 'private' else '#')
            params = ', '.join(method.get('params', []))
            lines.append(f'  {symbol} {method["name"]}({params}): {method["return_type"]}')

        lines.append('}')
        lines.append('')

    # Add relationships
    lines.append('')
    for cls in class_structs[:10]:
        class_name = cls['class_name']

        # Extends
        if cls.get('extends'):
            lines.append(f'{cls["extends"]} <|-- {class_name}')

        # Implements
        for impl in cls.get('implements', []):
            lines.append(f'{impl} <|.. {class_name}')

        # Associations (internal references)
        for ref in cls.get('internal_references', [])[:5]:
            lines.append(f'{class_name} --> {ref}')

    lines.append('')
    lines.append('@enduml')

    return '\n'.join(lines)

def generate_sequence_diagram(call_graphs, module_name):
    """Generate PlantUML sequence diagram"""
    lines = ['@startuml', f'title {module_name} - Sequence Diagram', '']

    lines.append('actor User')
    lines.append('')

    # Track participants
    participants = set()

    for cg in call_graphs[:5]:  # Limit to 5 call graphs
        source_class = cg['class']
        source_method = cg['method']

        participants.add(source_class)

        # Extract target classes
        for call in cg.get('calls', [])[:5]:
            target = call['to']
            if '.' in target:
                target_class = target.split('.')[0]
                target_method = target.split('.')[1] if len(target.split('.')) > 1 else 'method'
                participants.add(target_class)

    # Declare participants
    for participant in sorted(participants):
        lines.append(f'participant {participant}')

    lines.append('')

    # Add interactions
    for cg in call_graphs[:5]:
        source_class = cg['class']
        source_method = cg['method']

        lines.append(f'User -> {source_class}: {source_method}()')

        for call in cg.get('calls', [])[:5]:
            target = call['to']
            if '.' in target:
                target_class = target.split('.')[0]
                target_method = target.split('.')[1] if len(target.split('.')) > 1 else 'method'

                lines.append(f'{source_class} -> {target_class}: {target_method}()')

        lines.append('')

    lines.append('@enduml')

    return '\n'.join(lines)

def main():
    """Main entry point"""
    class_dir = '/home/user/biojava/analysis/A3_classes'
    callgraph_dir = '/home/user/biojava/analysis/A5_callgraphs'
    output_dir = '/home/user/biojava/analysis/A6_uml'

    os.makedirs(output_dir, exist_ok=True)

    # Generate class diagrams
    class_files = [f for f in os.listdir(class_dir) if f.endswith('_classes.json')]

    for class_file in class_files:
        module_name = class_file.replace('_classes.json', '')

        with open(os.path.join(class_dir, class_file), 'r') as f:
            class_structs = json.load(f)

        print(f"Generating class diagram for: {module_name}")

        uml = generate_class_diagram(class_structs, module_name)

        output_file = os.path.join(output_dir, f"{module_name}_class_diagram.puml")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(uml)

        print(f"  ✓ Saved: {output_file}")

    # Generate sequence diagrams
    callgraph_files = [f for f in os.listdir(callgraph_dir) if f.endswith('_callgraphs.json')]

    for cg_file in callgraph_files:
        module_name = cg_file.replace('_callgraphs.json', '')

        with open(os.path.join(callgraph_dir, cg_file), 'r') as f:
            call_graphs = json.load(f)

        print(f"Generating sequence diagram for: {module_name}")

        uml = generate_sequence_diagram(call_graphs, module_name)

        output_file = os.path.join(output_dir, f"{module_name}_sequence_diagram.puml")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(uml)

        print(f"  ✓ Saved: {output_file}")

    # Summary
    summary = {
        "project": "BioJava",
        "class_diagrams_generated": len(class_files),
        "sequence_diagrams_generated": len(callgraph_files),
        "analysis_level": "A6_UML_GENERATION",
        "next_step": "A7_BUSINESS_FLOWS"
    }

    summary_file = os.path.join(output_dir, "uml_generation_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print(f"\n✓ Summary saved: {summary_file}")

if __name__ == '__main__':
    main()
