#!/usr/bin/env python3
"""
PEACOCK COSMÉTICOS - CORREÇÃO DE CARREGAMENTO DE IMAGENS
Corrige URLs externas que estão causando erros 403 após otimização
"""

import os
import re
import glob

def fix_external_image_urls():
    """Corrige URLs externas para URLs locais em arquivos CSS"""
    print("🔧 Corrigindo URLs externas de imagens...")
    
    # Padrão para encontrar URLs externas
    external_url_pattern = r'url\("https://peacockcosmeticos\.com\.br/([^"]+)"\)'
    
    # Diretórios para verificar
    css_directories = [
        'wp-content/uploads/elementor/css/',
        'wp-content/themes/',
        'wp-content/plugins/',
        '.'
    ]
    
    fixed_files = []
    total_fixes = 0
    
    for directory in css_directories:
        if not os.path.exists(directory):
            continue
            
        # Encontrar todos os arquivos CSS
        css_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.css'):
                    css_files.append(os.path.join(root, file))
        
        for css_file in css_files:
            try:
                with open(css_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Contar quantas URLs externas existem
                external_urls = re.findall(external_url_pattern, content)
                
                if external_urls:
                    print(f"   📁 Corrigindo {css_file}: {len(external_urls)} URLs externas")
                    
                    # Substituir URLs externas por URLs locais
                    def replace_url(match):
                        relative_path = match.group(1)
                        return f'url("./{relative_path}")'
                    
                    new_content = re.sub(external_url_pattern, replace_url, content)
                    
                    # Salvar arquivo corrigido
                    with open(css_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    fixed_files.append(css_file)
                    total_fixes += len(external_urls)
                    
            except Exception as e:
                print(f"   ⚠️ Erro ao processar {css_file}: {e}")
                continue
    
    print(f"   ✅ {len(fixed_files)} arquivos corrigidos, {total_fixes} URLs fixadas")
    return fixed_files, total_fixes

def fix_html_image_references():
    """Corrige referências de imagens no HTML principal"""
    print("🔧 Corrigindo referências de imagens no HTML...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Padrões para URLs externas no HTML
    patterns = [
        # Background images em style attributes
        (r'background-image:\s*url\("https://peacockcosmeticos\.com\.br/([^"]+)"\)', 
         r'background-image: url("./\1")'),
        
        # Src attributes em img tags
        (r'src="https://peacockcosmeticos\.com\.br/([^"]+)"', 
         r'src="./\1"'),
        
        # Href attributes para recursos
        (r'href="https://peacockcosmeticos\.com\.br/([^"]+\.(css|js|png|jpg|jpeg|gif|webp))"', 
         r'href="./\1"'),
    ]
    
    fixes_made = 0
    for pattern, replacement in patterns:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            fixes_made += len(matches)
            print(f"   🔄 Corrigidas {len(matches)} referências do tipo: {pattern[:50]}...")
    
    if fixes_made > 0:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ {fixes_made} referências corrigidas no HTML")
    else:
        print("   ℹ️ Nenhuma referência externa encontrada no HTML")
    
    return fixes_made

def verify_image_paths():
    """Verifica se os caminhos das imagens existem localmente"""
    print("🔍 Verificando caminhos de imagens...")
    
    # Encontrar todas as referências de imagens
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Verificar arquivos CSS também
    css_files = []
    for root, dirs, files in os.walk('wp-content/uploads/elementor/css/'):
        for file in files:
            if file.endswith('.css'):
                css_files.append(os.path.join(root, file))
    
    all_image_refs = set()
    
    # Extrair referências do HTML
    html_patterns = [
        r'src="\./(wp-content/[^"]+\.(png|jpg|jpeg|gif|webp))"',
        r'url\("\./(wp-content/[^"]+\.(png|jpg|jpeg|gif|webp))"\)',
    ]
    
    for pattern in html_patterns:
        matches = re.findall(pattern, html_content)
        for match in matches:
            if isinstance(match, tuple):
                all_image_refs.add(match[0])
            else:
                all_image_refs.add(match)
    
    # Extrair referências dos CSS
    for css_file in css_files:
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            css_patterns = [
                r'url\("\./(wp-content/[^"]+\.(png|jpg|jpeg|gif|webp))"\)',
            ]
            
            for pattern in css_patterns:
                matches = re.findall(pattern, css_content)
                for match in matches:
                    if isinstance(match, tuple):
                        all_image_refs.add(match[0])
                    else:
                        all_image_refs.add(match)
        except:
            continue
    
    # Verificar se os arquivos existem
    missing_files = []
    existing_files = []
    
    for image_path in all_image_refs:
        if os.path.exists(image_path):
            existing_files.append(image_path)
        else:
            missing_files.append(image_path)
    
    print(f"   ✅ {len(existing_files)} imagens encontradas localmente")
    if missing_files:
        print(f"   ❌ {len(missing_files)} imagens não encontradas:")
        for missing in missing_files[:5]:  # Mostrar apenas as primeiras 5
            print(f"      📄 {missing}")
        if len(missing_files) > 5:
            print(f"      ... e mais {len(missing_files) - 5} arquivos")
    
    return existing_files, missing_files

def create_missing_image_placeholders():
    """Cria placeholders para imagens que não existem"""
    print("🖼️ Criando placeholders para imagens ausentes...")
    
    existing_files, missing_files = verify_image_paths()
    
    if not missing_files:
        print("   ℹ️ Todas as imagens existem localmente")
        return 0
    
    placeholders_created = 0
    
    for missing_file in missing_files:
        # Criar diretório se não existir
        directory = os.path.dirname(missing_file)
        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory, exist_ok=True)
            except:
                continue
        
        # Criar um placeholder simples (arquivo vazio por enquanto)
        try:
            # Verificar se existe uma imagem similar no mesmo diretório
            base_name = os.path.basename(missing_file)
            dir_name = os.path.dirname(missing_file)
            
            if os.path.exists(dir_name):
                # Procurar por arquivos similares
                similar_files = []
                for file in os.listdir(dir_name):
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                        similar_files.append(os.path.join(dir_name, file))
                
                if similar_files:
                    # Copiar um arquivo similar como placeholder
                    import shutil
                    shutil.copy2(similar_files[0], missing_file)
                    placeholders_created += 1
                    print(f"   📋 Placeholder criado: {missing_file}")
                
        except Exception as e:
            print(f"   ⚠️ Erro ao criar placeholder para {missing_file}: {e}")
            continue
    
    print(f"   ✅ {placeholders_created} placeholders criados")
    return placeholders_created

def test_image_loading():
    """Testa se as correções resolveram os problemas"""
    print("🧪 Testando carregamento de imagens...")
    
    # Verificar se ainda existem URLs externas
    external_refs = 0
    
    # Verificar HTML
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    external_patterns = [
        r'https://peacockcosmeticos\.com\.br/',
        r'src="http[s]?://[^"]*peacockcosmeticos\.com\.br[^"]*"',
        r'url\("http[s]?://[^"]*peacockcosmeticos\.com\.br[^"]*"\)',
    ]
    
    for pattern in external_patterns:
        matches = re.findall(pattern, html_content)
        external_refs += len(matches)
    
    # Verificar CSS
    css_files = []
    for root, dirs, files in os.walk('wp-content/uploads/elementor/css/'):
        for file in files:
            if file.endswith('.css'):
                css_files.append(os.path.join(root, file))
    
    for css_file in css_files:
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            for pattern in external_patterns:
                matches = re.findall(pattern, css_content)
                external_refs += len(matches)
        except:
            continue
    
    if external_refs == 0:
        print("   ✅ Nenhuma referência externa encontrada")
        return True
    else:
        print(f"   ❌ Ainda existem {external_refs} referências externas")
        return False

def main():
    """Executa todas as correções de carregamento de imagens"""
    print("🎯 CORRIGINDO CARREGAMENTO DE IMAGENS - PEACOCK COSMÉTICOS\n")
    
    # Backup do estado atual
    if not os.path.exists('index_image_fix_backup.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        with open('index_image_fix_backup.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("📋 Backup criado: index_image_fix_backup.html")
    
    # Executar correções
    fixed_files, total_fixes = fix_external_image_urls()
    html_fixes = fix_html_image_references()
    existing_files, missing_files = verify_image_paths()
    placeholders_created = create_missing_image_placeholders()
    test_passed = test_image_loading()
    
    print("\n🎉 CORREÇÃO DE IMAGENS COMPLETA!")
    print("📊 Resultados:")
    print(f"   🔧 Arquivos CSS corrigidos: {len(fixed_files)}")
    print(f"   🔄 URLs externas corrigidas: {total_fixes}")
    print(f"   📄 Correções no HTML: {html_fixes}")
    print(f"   ✅ Imagens existentes: {len(existing_files)}")
    print(f"   ❌ Imagens ausentes: {len(missing_files)}")
    print(f"   📋 Placeholders criados: {placeholders_created}")
    print(f"   🧪 Teste final: {'✅ PASSOU' if test_passed else '❌ FALHOU'}")
    
    if fixed_files:
        print(f"\n📁 Arquivos corrigidos:")
        for file in fixed_files[:5]:  # Mostrar apenas os primeiros 5
            print(f"   📄 {file}")
        if len(fixed_files) > 5:
            print(f"   ... e mais {len(fixed_files) - 5} arquivos")

if __name__ == "__main__":
    main()
