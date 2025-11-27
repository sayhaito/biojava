#!/usr/bin/env python3
"""
A4 Method Logic Flow Analysis Script - BioJava
Analyzes method implementations and generates method_flow.json
"""
import os
import json
import re
from pathlib import Path

def extract_method_body(content, method_name):
    """Extract the body of a specific method"""
    # Remove comments
    content_clean = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content_clean = re.sub(r'//.*?\n', '\n', content_clean)

    # Find method declaration
    pattern = rf'(?:public|private|protected)\s+(?:static\s+)?(?:final\s+)?[\w<>\[\]]+\s+{re.escape(method_name)}\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{{'

    match = re.search(pattern, content_clean)
    if not match:
        return None

    # Find matching closing brace
    start = match.end() - 1
    brace_count = 1
    i = start + 1

    while i < len(content_clean) and brace_count > 0:
        if content_clean[i] == '{':
            brace_count += 1
        elif content_clean[i] == '}':
            brace_count -= 1
        i += 1

    if brace_count == 0:
        return content_clean[start+1:i-1]

    return None

def analyze_method_steps(method_body):
    """Extract ordered execution steps from method body"""
    if not method_body:
        return []

    steps = []

    # Split into lines and filter
    lines = [line.strip() for line in method_body.split('\n') if line.strip()]

    for line in lines:
        # Skip certain patterns
        if line.startswith('}') or line.startswith('{'):
            continue

        # Method calls
        if re.search(r'\w+\s*\(', line):
            steps.append(line[:100])  # Limit length

        # Variable assignments
        elif '=' in line and not line.startswith('if') and not line.startswith('for'):
            steps.append(line[:100])

        # return statements
        elif line.startswith('return'):
            steps.append(line[:100])

        if len(steps) >= 20:  # Limit steps
            break

    return steps

def analyze_branches(method_body):
    """Extract conditional branches (if/else)"""
    if not method_body:
        return []

    branches = []

    # Find if statements
    if_pattern = r'if\s*\((.*?)\)\s*\{'

    for match in re.finditer(if_pattern, method_body):
        condition = match.group(1).strip()

        # Try to find the true path (simplified)
        true_path = ["unknown_or_not_in_code"]
        false_path = ["unknown_or_not_in_code"]

        branches.append({
            "condition": condition[:100],  # Limit length
            "true_path": true_path,
            "false_path": false_path
        })

        if len(branches) >= 5:  # Limit branches
            break

    return branches

def analyze_loops(method_body):
    """Extract loop constructs"""
    if not method_body:
        return []

    loops = []

    # For loops
    for_pattern = r'for\s*\((.*?)\)\s*\{'
    for match in re.finditer(for_pattern, method_body):
        loops.append({
            "type": "for",
            "declaration": match.group(1).strip()[:100]
        })

    # While loops
    while_pattern = r'while\s*\((.*?)\)\s*\{'
    for match in re.finditer(while_pattern, method_body):
        loops.append({
            "type": "while",
            "condition": match.group(1).strip()[:100]
        })

    # Enhanced for loops
    foreach_pattern = r'for\s*\(.*?:\s*(.*?)\)\s*\{'
    for match in re.finditer(foreach_pattern, method_body):
        loops.append({
            "type": "foreach",
            "collection": match.group(1).strip()[:100]
        })

    return loops[:5]  # Limit to 5

def analyze_exceptions(method_body, content):
    """Extract exception handling"""
    exceptions = []

    # From method signature
    throws_pattern = r'throws\s+([\w,\s]+)\s*\{'
    match = re.search(throws_pattern, content)
    if match:
        thrown = [e.strip() for e in match.group(1).split(',')]
        exceptions.extend(thrown)

    # Catch blocks
    if method_body:
        catch_pattern = r'catch\s*\((.*?)\)'
        for match in re.finditer(catch_pattern, method_body):
            exception_type = match.group(1).strip().split()[0]
            if exception_type not in exceptions:
                exceptions.append(exception_type)

        # Throw statements
        throw_pattern = r'throw\s+new\s+(\w+)'
        for match in re.finditer(throw_pattern, method_body):
            exception_type = match.group(1)
            if exception_type not in exceptions:
                exceptions.append(exception_type)

    return list(set(exceptions))[:5]  # Limit to 5 unique

def analyze_external_calls(method_body):
    """Extract external method calls"""
    if not method_body:
        return []

    external_calls = []

    # Pattern for method calls
    call_pattern = r'(\w+)\.(\w+)\s*\('

    for match in re.finditer(call_pattern, method_body):
        obj = match.group(1)
        method = match.group(2)

        # Filter out common Java methods
        if method not in ['toString', 'equals', 'hashCode', 'get', 'set', 'size', 'length']:
            call = f"{obj}.{method}()"
            if call not in external_calls:
                external_calls.append(call)

    return external_calls[:15]  # Limit to 15

def analyze_method(file_path, class_name, method_name):
    """Analyze a single method"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        method_body = extract_method_body(content, method_name)

        if not method_body:
            return None

        steps = analyze_method_steps(method_body)
        branches = analyze_branches(method_body)
        loops = analyze_loops(method_body)
        exceptions = analyze_exceptions(method_body, content)
        external_calls = analyze_external_calls(method_body)

        method_flow = {
            "class": class_name,
            "method": method_name,
            "steps": steps,
            "branches": branches,
            "loops": loops,
            "exceptions": exceptions,
            "external_calls": external_calls,
            "next_step": "continue"
        }

        return method_flow

    except Exception as e:
        print(f"Error analyzing method {method_name} in {file_path}: {e}")
        return None

def select_important_methods(class_struct):
    """Select important methods to analyze from a class"""
    methods = class_struct.get('methods', [])

    important = []
    keywords = ['parse', 'read', 'write', 'load', 'save', 'process', 'execute',
                'calculate', 'build', 'create', 'get', 'set', 'init', 'run']

    for method in methods:
        name = method['name'].lower()
        # Skip trivial getters/setters with empty params
        if (name.startswith('get') or name.startswith('set')) and len(method.get('params', [])) <= 1:
            if len(important) < 3:  # Keep some getters/setters
                important.append(method)
        elif any(kw in name for kw in keywords):
            important.append(method)

    return important[:10]  # Limit to 10 methods per class

def main():
    """Main entry point"""
    biojava_root = '/home/user/biojava'
    class_dir = '/home/user/biojava/analysis/A3_classes'
    output_dir = '/home/user/biojava/analysis/A4_methods'

    os.makedirs(output_dir, exist_ok=True)

    # Read all class analysis files
    class_files = [f for f in os.listdir(class_dir) if f.endswith('_classes.json')]

    total_analyzed = 0

    for class_file in class_files:
        module_name = class_file.replace('_classes.json', '')

        with open(os.path.join(class_dir, class_file), 'r') as f:
            class_structs = json.load(f)

        print(f"\nAnalyzing methods in module: {module_name}")

        module_methods = []

        for class_struct in class_structs[:5]:  # Limit to 5 classes per module
            class_name = class_struct['class_name']
            package = class_struct['package']

            # Construct file path
            package_path = package.replace('.', '/')
            file_path = os.path.join(biojava_root, module_name, 'src/main/java',
                                      package_path, f"{class_name}.java")

            if not os.path.exists(file_path):
                continue

            # Select important methods
            important_methods = select_important_methods(class_struct)

            for method in important_methods[:3]:  # Max 3 methods per class
                method_name = method['name']

                method_flow = analyze_method(file_path, class_name, method_name)

                if method_flow:
                    module_methods.append(method_flow)
                    print(f"  ✓ {class_name}.{method_name}()")
                    total_analyzed += 1

        # Save module method flows
        if module_methods:
            output_file = os.path.join(output_dir, f"{module_name}_methods.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(module_methods, f, indent=2)

    # Summary
    summary = {
        "project": "BioJava",
        "total_methods_analyzed": total_analyzed,
        "analysis_level": "A4_METHOD_LOGIC",
        "next_step": "A5_CALL_GRAPH"
    }

    summary_file = os.path.join(output_dir, "method_analysis_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print(f"\n✓ Total methods analyzed: {total_analyzed}")
    print(f"✓ Summary saved: {summary_file}")

if __name__ == '__main__':
    main()
