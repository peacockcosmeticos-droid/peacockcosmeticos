#!/usr/bin/env python3
"""
PEACOCK COSMÉTICOS - CORREÇÃO DE SRCSET E LINKS
Corrige problemas específicos em srcset e links que estão causando erros 403
"""

import os
import re

def fix_srcset_attributes():
    """Corrige atributos srcset malformados"""
    print("🔧 Corrigindo atributos srcset...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Padrão para srcset com caminhos malformados
    # Exemplo: "wp-content/uploads/2025/08/3.png 600w, ./wp-content/uploads/"
    srcset_pattern = r'srcset="([^"]*wp-content/uploads/[^"]*?),\s*\./wp-content/uploads/[^"]*?"'
    
    def fix_srcset(match):
        srcset_value = match.group(1)
        # Remover a parte malformada no final
        cleaned_srcset = re.sub(r',\s*\./wp-content/uploads/[^"]*$', '', srcset_value)
        return f'srcset="{cleaned_srcset}"'
    
    # Aplicar correção
    new_content = re.sub(srcset_pattern, fix_srcset, content)
    
    # Contar quantas correções foram feitas
    fixes = len(re.findall(srcset_pattern, content))
    
    if fixes > 0:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"   ✅ {fixes} atributos srcset corrigidos")
    else:
        print("   ℹ️ Nenhum srcset malformado encontrado")
    
    return fixes

def fix_link_tags():
    """Corrige tags link malformadas"""
    print("🔧 Corrigindo tags link...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Padrão para links malformados que se estendem além do que deveriam
    # Exemplo: href='./wp-content/uploads/elementor/css/post-16.css?ver=1755603765' media='all' /><link rel='stylesheet' id='elementor-post-74-css' href='./wp-content/uploads/
    link_pattern = r"href='([^']*\.css[^']*?)'\s+media='all'\s*/><link[^>]*href='\.\/wp-content\/uploads\/[^']*'"
    
    def fix_link(match):
        href_value = match.group(1)
        return f"href='{href_value}' media='all' />"
    
    # Aplicar correção
    new_content = re.sub(link_pattern, fix_link, content)
    
    # Contar quantas correções foram feitas
    fixes = len(re.findall(link_pattern, content))
    
    if fixes > 0:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"   ✅ {fixes} tags link corrigidas")
    else:
        print("   ℹ️ Nenhuma tag link malformada encontrada")
    
    return fixes

def fix_broken_html_structure():
    """Corrige estrutura HTML quebrada"""
    print("🔧 Corrigindo estrutura HTML quebrada...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    fixes = 0
    
    # Corrigir tags link quebradas que se estendem incorretamente
    broken_link_patterns = [
        # Padrão 1: Link que se estende além do fechamento
        (r"(<link[^>]*href='[^']*\.css[^']*?'[^>]*/>)<link[^>]*href='\.\/wp-content\/uploads\/[^']*'[^>]*>", 
         r'\1'),
        
        # Padrão 2: Srcset que termina abruptamente
        (r'srcset="([^"]*),\s*\./wp-content/uploads/[^"]*?"', 
         r'srcset="\1"'),
        
        # Padrão 3: Atributos duplicados ou malformados
        (r'(\s+wp-content/uploads/[^"]*?"),\s*\./wp-content/uploads/[^"]*?"', 
         r'\1"'),
    ]
    
    for pattern, replacement in broken_link_patterns:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            fixes += len(matches)
            print(f"   🔄 Corrigidas {len(matches)} ocorrências do padrão")
    
    if content != original_content:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ {fixes} correções de estrutura aplicadas")
    else:
        print("   ℹ️ Nenhuma estrutura quebrada encontrada")
    
    return fixes

def clean_malformed_urls():
    """Remove URLs malformadas que estão causando 403"""
    print("🧹 Limpando URLs malformadas...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Padrões específicos que estão causando os erros 403
    malformed_url_patterns = [
        # URLs que terminam com wp-content/uploads/ sem arquivo
        r'url\("\.\/wp-content\/uploads\/"\)',
        r'src="\.\/wp-content\/uploads\/"',
        r'href="\.\/wp-content\/uploads\/"',
        
        # Caminhos duplicados específicos vistos nos logs
        r'\/wp-content\/uploads\/elementor\/css\/wp-content\/uploads\/',
        
        # Srcset que termina com vírgula e caminho incompleto
        r',\s*\.\/wp-content\/uploads\/[^"]*?"',
    ]
    
    fixes = 0
    for pattern in malformed_url_patterns:
        matches = re.findall(pattern, content)
        if matches:
            # Remover essas URLs malformadas
            content = re.sub(pattern, '', content)
            fixes += len(matches)
            print(f"   🗑️ Removidas {len(matches)} URLs malformadas")
    
    # Limpar vírgulas órfãs em srcset
    content = re.sub(r'srcset="([^"]*),\s*"', r'srcset="\1"', content)
    
    if content != original_content:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ {fixes} URLs malformadas removidas")
    else:
        print("   ℹ️ Nenhuma URL malformada encontrada")
    
    return fixes

def verify_403_errors_fixed():
    """Verifica se os erros 403 específicos foram corrigidos"""
    print("🔍 Verificando se os erros 403 foram corrigidos...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Procurar pelos caminhos específicos que estavam causando 403
    problematic_paths = [
        'wp-content/uploads/elementor/css/wp-content/uploads/2024/10/peecock-03.png',
        'wp-content/uploads/elementor/css/wp-content/uploads/2024/10/bg01.jpg',
        '/wp-content/uploads/elementor/css/wp-content/uploads/',
    ]
    
    errors_found = []
    for path in problematic_paths:
        if path in content:
            errors_found.append(path)
    
    if errors_found:
        print(f"   ❌ Ainda existem {len(errors_found)} caminhos problemáticos:")
        for error in errors_found:
            print(f"      📄 {error}")
        return False
    else:
        print("   ✅ Nenhum caminho problemático encontrado")
        return True

def main():
    """Executa todas as correções específicas"""
    print("🎯 CORRIGINDO SRCSET E LINKS - PEACOCK COSMÉTICOS\n")
    
    # Backup do estado atual
    if not os.path.exists('index_srcset_fix_backup.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        with open('index_srcset_fix_backup.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("📋 Backup criado: index_srcset_fix_backup.html")
    
    # Executar correções
    srcset_fixes = fix_srcset_attributes()
    link_fixes = fix_link_tags()
    structure_fixes = fix_broken_html_structure()
    url_fixes = clean_malformed_urls()
    verification_passed = verify_403_errors_fixed()
    
    print("\n🎉 CORREÇÃO DE SRCSET E LINKS COMPLETA!")
    print("📊 Resultados:")
    print(f"   🖼️ Srcset corrigidos: {srcset_fixes}")
    print(f"   🔗 Links corrigidos: {link_fixes}")
    print(f"   🏗️ Estruturas corrigidas: {structure_fixes}")
    print(f"   🧹 URLs malformadas removidas: {url_fixes}")
    print(f"   🧪 Verificação 403: {'✅ PASSOU' if verification_passed else '❌ FALHOU'}")
    
    total_fixes = srcset_fixes + link_fixes + structure_fixes + url_fixes
    if total_fixes > 0:
        print(f"\n💡 Total de {total_fixes} correções aplicadas!")
        print("🔄 Recomendado: Testar o site novamente para verificar se os erros 403 foram resolvidos")
    else:
        print("\n💡 Nenhuma correção adicional necessária")

if __name__ == "__main__":
    main()
