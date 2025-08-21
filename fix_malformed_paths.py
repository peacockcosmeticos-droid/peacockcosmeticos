#!/usr/bin/env python3
"""
PEACOCK COSMÉTICOS - CORREÇÃO DE CAMINHOS MALFORMADOS
Corrige caminhos duplicados que estão causando erros 403
"""

import os
import re
import glob

def fix_malformed_css_paths():
    """Corrige caminhos malformados em arquivos CSS"""
    print("🔧 Corrigindo caminhos malformados em CSS...")
    
    # Padrões para encontrar caminhos malformados
    malformed_patterns = [
        # Padrão: wp-content/uploads/elementor/css/wp-content/uploads/...
        (r'url\("([^"]*wp-content/uploads/elementor/css/)(wp-content/uploads/[^"]+)"\)', 
         r'url("./\2")'),
        
        # Padrão: ./wp-content/uploads/elementor/css/wp-content/uploads/...
        (r'url\("(\./wp-content/uploads/elementor/css/)(wp-content/uploads/[^"]+)"\)', 
         r'url("./\2")'),
        
        # Padrão geral de duplicação de paths
        (r'url\("([^"]*)(wp-content/uploads/[^"]*)(wp-content/uploads/[^"]+)"\)', 
         r'url("./\3")'),
    ]
    
    fixed_files = []
    total_fixes = 0
    
    # Encontrar todos os arquivos CSS
    css_files = []
    for root, dirs, files in os.walk('.'):
        if any(skip in root for skip in ['.git', '__pycache__']):
            continue
        for file in files:
            if file.endswith('.css'):
                css_files.append(os.path.join(root, file))
    
    for css_file in css_files:
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_fixes = 0
            
            # Aplicar cada padrão de correção
            for pattern, replacement in malformed_patterns:
                matches = re.findall(pattern, content)
                if matches:
                    content = re.sub(pattern, replacement, content)
                    file_fixes += len(matches)
                    print(f"   🔄 {css_file}: Corrigidas {len(matches)} ocorrências do padrão")
            
            # Salvar se houve mudanças
            if content != original_content:
                with open(css_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed_files.append(css_file)
                total_fixes += file_fixes
                print(f"   ✅ {css_file}: {file_fixes} correções aplicadas")
                
        except Exception as e:
            print(f"   ⚠️ Erro ao processar {css_file}: {e}")
            continue
    
    print(f"   📊 Total: {len(fixed_files)} arquivos corrigidos, {total_fixes} caminhos fixados")
    return fixed_files, total_fixes

def fix_malformed_html_paths():
    """Corrige caminhos malformados no HTML"""
    print("🔧 Corrigindo caminhos malformados no HTML...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Padrões para caminhos malformados no HTML
    malformed_patterns = [
        # href com caminhos duplicados
        (r'href="([^"]*wp-content/uploads/elementor/css/)(wp-content/uploads/[^"]+)"', 
         r'href="./\2"'),
        
        # src com caminhos duplicados
        (r'src="([^"]*wp-content/uploads/elementor/css/)(wp-content/uploads/[^"]+)"', 
         r'src="./\2"'),
        
        # background-image com caminhos duplicados
        (r'background-image:\s*url\("([^"]*wp-content/uploads/elementor/css/)(wp-content/uploads/[^"]+)"\)', 
         r'background-image: url("./\2")'),
    ]
    
    total_fixes = 0
    for pattern, replacement in malformed_patterns:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            total_fixes += len(matches)
            print(f"   🔄 Corrigidas {len(matches)} ocorrências no HTML")
    
    if content != original_content:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ {total_fixes} correções aplicadas no HTML")
    else:
        print("   ℹ️ Nenhum caminho malformado encontrado no HTML")
    
    return total_fixes

def verify_no_malformed_paths():
    """Verifica se ainda existem caminhos malformados"""
    print("🔍 Verificando se ainda existem caminhos malformados...")
    
    malformed_found = []
    
    # Verificar HTML
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Padrões para detectar caminhos malformados
    detection_patterns = [
        r'wp-content/uploads/elementor/css/wp-content/uploads/',
        r'wp-content/uploads/[^"]*wp-content/uploads/',
        r'url\("[^"]*wp-content/[^"]*wp-content/uploads/',
    ]
    
    for pattern in detection_patterns:
        matches = re.findall(pattern, html_content)
        if matches:
            malformed_found.extend(matches)
    
    # Verificar CSS
    css_files = []
    for root, dirs, files in os.walk('.'):
        if any(skip in root for skip in ['.git', '__pycache__']):
            continue
        for file in files:
            if file.endswith('.css'):
                css_files.append(os.path.join(root, file))
    
    for css_file in css_files:
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            for pattern in detection_patterns:
                matches = re.findall(pattern, css_content)
                if matches:
                    malformed_found.extend(matches)
                    print(f"   ⚠️ Caminhos malformados encontrados em {css_file}")
        except:
            continue
    
    if malformed_found:
        print(f"   ❌ {len(malformed_found)} caminhos malformados ainda encontrados")
        unique_malformed = list(set(malformed_found))[:5]  # Mostrar apenas os primeiros 5 únicos
        for malformed in unique_malformed:
            print(f"      📄 {malformed}")
        return False
    else:
        print("   ✅ Nenhum caminho malformado encontrado")
        return True

def clean_duplicate_slashes():
    """Remove barras duplas em caminhos"""
    print("🧹 Limpando barras duplas em caminhos...")
    
    files_to_check = ['index.html']
    
    # Adicionar arquivos CSS
    for root, dirs, files in os.walk('.'):
        if any(skip in root for skip in ['.git', '__pycache__']):
            continue
        for file in files:
            if file.endswith('.css'):
                files_to_check.append(os.path.join(root, file))
    
    total_fixes = 0
    
    for file_path in files_to_check:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Corrigir barras duplas em URLs
            content = re.sub(r'url\("([^"]*?)//+([^"]*?)"\)', r'url("\1/\2")', content)
            content = re.sub(r'src="([^"]*?)//+([^"]*?)"', r'src="\1/\2"', content)
            content = re.sub(r'href="([^"]*?)//+([^"]*?)"', r'href="\1/\2"', content)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                total_fixes += 1
                print(f"   ✅ Barras duplas corrigidas em {file_path}")
        except:
            continue
    
    print(f"   📊 {total_fixes} arquivos com barras duplas corrigidas")
    return total_fixes

def main():
    """Executa todas as correções de caminhos malformados"""
    print("🎯 CORRIGINDO CAMINHOS MALFORMADOS - PEACOCK COSMÉTICOS\n")
    
    # Backup do estado atual
    if not os.path.exists('index_malformed_fix_backup.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        with open('index_malformed_fix_backup.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("📋 Backup criado: index_malformed_fix_backup.html")
    
    # Executar correções
    css_files, css_fixes = fix_malformed_css_paths()
    html_fixes = fix_malformed_html_paths()
    slash_fixes = clean_duplicate_slashes()
    verification_passed = verify_no_malformed_paths()
    
    print("\n🎉 CORREÇÃO DE CAMINHOS MALFORMADOS COMPLETA!")
    print("📊 Resultados:")
    print(f"   🔧 Arquivos CSS corrigidos: {len(css_files)}")
    print(f"   🔄 Caminhos CSS corrigidos: {css_fixes}")
    print(f"   📄 Caminhos HTML corrigidos: {html_fixes}")
    print(f"   🧹 Barras duplas corrigidas: {slash_fixes}")
    print(f"   🧪 Verificação final: {'✅ PASSOU' if verification_passed else '❌ FALHOU'}")
    
    if css_files:
        print(f"\n📁 Arquivos CSS corrigidos:")
        for file in css_files[:5]:  # Mostrar apenas os primeiros 5
            print(f"   📄 {file}")
        if len(css_files) > 5:
            print(f"   ... e mais {len(css_files) - 5} arquivos")

if __name__ == "__main__":
    main()
