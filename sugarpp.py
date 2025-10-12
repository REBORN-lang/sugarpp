#!/usr/bin/env python3
import re, sys, os
from pathlib import Path

# sugar++
'''
TODO LIST:
- Comment code (HIGH PRIORITY)
- Fix indentation in generated .cpp file (Low priority)
'''

if len(sys.argv) < 2:
    print("usage → sugarpp <file.spp> [output.cpp]")
    sys.exit(1)

inp = Path(sys.argv[1])
outp = Path(sys.argv[2]) if len(sys.argv) > 2 else inp.with_suffix('.cpp')

ctrl_pattern = re.compile(r'^(\s*)(if|while|for|switch)\s+([^{(].*?)\s*\{?$')
include_pattern = re.compile(r'^\s*include\s+([A-Za-z0-9_]+)')

main_pattern = re.compile(r'^\s*main\s*(?:\((.*)\)|:\s*int\s*\((.*)\))')

let_func_def_pattern = re.compile(r'^(\s*)let\s+([A-Za-z_]\w*)\s*:\s*([\w:<>*&]+)\s*\((.*)\)\s*\{?')
let_func_proto_pattern = re.compile(r'^(\s*)let\s+([A-Za-z_]\w*)\s*:\s*([\w:<>*&]+)\s*\((.*)\);')

let_typed_pattern = re.compile(
    r'^(\s*)(?:(?P<kw>(?:const|static|inline|volatile)\s+)+)?let\s+([A-Za-z_]\w*(?:\[[^\]]*\])*)\s*:\s*([\w:<>*&]+)\s*(?:=\s*(.*))?;'
)
let_infer_pattern = re.compile(r'^(\s*)let\s+([A-Za-z_]\w*)\s*:=\s*(.*);')
let_plain_pattern = re.compile(r'^(\s*)let\s+([A-Za-z_]\w*)\s*;')

def conv_params(params: str) -> str:
    if not params or not params.strip():
        return ""
    out = []
    for p in params.split(','):
        p = p.strip()
        if ':' in p:
            name, typ = map(str.strip, p.split(':', 1))
            if typ.startswith('**'):
                typ_name = typ[2:] + '**'
            elif typ.startswith('*'):
                typ_name = typ[1:] + '*'
            else:
                typ_name = typ
            out.append(f"{typ_name} {name}")
        else:
            out.append(p)
    return ', '.join(out)

with inp.open() as f_in:
    lines = f_in.readlines()

with outp.open('w') as f_out:
    i = 0
    while i < len(lines):
        l = lines[i].rstrip('\n')
        next_line = lines[i+1].strip() if i+1 < len(lines) else ''

        l = re.sub(r'^\s*elif\s+', 'else if ', l)

        m_ctrl = re.match(r'^(\s*)(else\s+)?(if|while|for|switch)\s+([^{(].*?)\s*\{?$', l)
        if m_ctrl:
            indent = m_ctrl.group(1)
            else_part = m_ctrl.group(2) or ''
            keyword = m_ctrl.group(3)
            cond = m_ctrl.group(4).strip()
            l = f"{indent}{else_part}{keyword} ({cond})"
            if not l.rstrip().endswith('{') and next_line != '{':
                l += '{'

        l = include_pattern.sub(lambda m: f"#include <{m.group(1)}>", l)

        m_main = main_pattern.match(l)
        if m_main:
            params = m_main.group(1) or m_main.group(2) or ''
            l = f"int main({conv_params(params)})"
            if not l.rstrip().endswith('{') and next_line != '{':
                l += '{'

        m_proto = let_func_proto_pattern.match(l)
        if m_proto:
            l = f"{m_proto.group(1)}{m_proto.group(3)} {m_proto.group(2)}({conv_params(m_proto.group(4))});"

        m_def = let_func_def_pattern.match(l)
        if m_def:
            if not l.rstrip().endswith(';'):
                l = f"{m_def.group(1)}{m_def.group(3)} {m_def.group(2)}({conv_params(m_def.group(4))})"
                if not l.rstrip().endswith('{') and next_line != '{':
                    l += '{'

        def repl_typed(m):
            kw = m.group('kw') or ''
            return f"{kw}{m.group(4)} {m.group(3)}" + (f" = {m.group(5)};" if m.group(5) else ";")

        l = let_typed_pattern.sub(repl_typed, l)
        l = let_infer_pattern.sub(lambda m: f"{m.group(1)}auto {m.group(2)} = {m.group(3)};", l)
        l = let_plain_pattern.sub(lambda m: f"{m.group(1)}auto {m.group(2)};", l)

        f_out.write(l + '\n')
        i += 1

print(f"→ done!\n→ {inp.name} → {outp.name}")

#compileAnsw = input("→ compile? (Y/n) ")
#compilePath = f"g++ -std=c++23 -o {outp.name.replace('.cpp','')} {outp.name}"
#
#if compileAnsw.upper() == "Y" or compileAnsw == "":
#    os.system(compilePath)
#else:
#    sys.exit(0)
