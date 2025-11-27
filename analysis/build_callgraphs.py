#!/usr/bin/env python3
"""
A5 Call Graph Builder - BioJava
Builds call graphs from method flow analysis
"""
import os
import json

def build_call_graph(method_flow):
    """Build call graph from method flow"""
    class_name = method_flow['class']
    method_name = method_flow['method']
    external_calls = method_flow.get('external_calls', [])

    calls = []

    # Create call edges
    for call in external_calls:
        # Parse the call format "object.method()"
        if '.' in call:
            target = call.replace('()', '')
            calls.append({
                "from": f"{class_name}.{method_name}",
                "to": target
            })

    call_graph = {
        "class": class_name,
        "method": method_name,
        "calls": calls,
        "depth": 1,
        "next_step": "continue"
    }

    return call_graph

def main():
    """Main entry point"""
    method_dir = '/home/user/biojava/analysis/A4_methods'
    output_dir = '/home/user/biojava/analysis/A5_callgraphs'

    os.makedirs(output_dir, exist_ok=True)

    # Read all method analysis files
    method_files = [f for f in os.listdir(method_dir) if f.endswith('_methods.json')]

    total_graphs = 0

    for method_file in method_files:
        module_name = method_file.replace('_methods.json', '')

        with open(os.path.join(method_dir, method_file), 'r') as f:
            method_flows = json.load(f)

        print(f"\nBuilding call graphs for: {module_name}")

        module_graphs = []

        for method_flow in method_flows:
            call_graph = build_call_graph(method_flow)

            if call_graph['calls']:  # Only save if there are calls
                module_graphs.append(call_graph)
                print(f"  ✓ {call_graph['class']}.{call_graph['method']}")
                total_graphs += 1

        # Save module call graphs
        if module_graphs:
            output_file = os.path.join(output_dir, f"{module_name}_callgraphs.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(module_graphs, f, indent=2)

    # Summary
    summary = {
        "project": "BioJava",
        "total_call_graphs": total_graphs,
        "analysis_level": "A5_CALL_GRAPH",
        "next_step": "A6_UML_GENERATION"
    }

    summary_file = os.path.join(output_dir, "callgraph_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print(f"\n✓ Total call graphs built: {total_graphs}")
    print(f"✓ Summary saved: {summary_file}")

if __name__ == '__main__':
    main()
