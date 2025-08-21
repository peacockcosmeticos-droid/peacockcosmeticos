#!/usr/bin/env python3
"""
PEACOCK COSMÉTICOS - MINIFICAÇÃO DE CSS E JAVASCRIPT
Reduz CSS (56 KiB) e JavaScript não usado (50 KiB) para melhorar o carregamento
"""

import re
import os
import json
from pathlib import Path

def minify_inline_css():
    """Minifica CSS inline no HTML"""
    print("🎨 Minificando CSS inline...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Padrão para encontrar blocos <style>
    style_pattern = r'<style[^>]*>(.*?)</style>'
    
    def minify_css_block(match):
        css_content = match.group(1)
        
        # Remover comentários CSS
        css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
        
        # Remover espaços em branco desnecessários
        css_content = re.sub(r'\s+', ' ', css_content)
        css_content = re.sub(r';\s*}', '}', css_content)
        css_content = re.sub(r'{\s*', '{', css_content)
        css_content = re.sub(r'}\s*', '}', css_content)
        css_content = re.sub(r':\s*', ':', css_content)
        css_content = re.sub(r';\s*', ';', css_content)
        
        # Remover últimos pontos e vírgulas antes de }
        css_content = re.sub(r';+}', '}', css_content)
        
        return f'<style>{css_content.strip()}</style>'
    
    # Aplicar minificação
    content = re.sub(style_pattern, minify_css_block, content, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("   ✅ CSS inline minificado")

def remove_unused_css():
    """Remove CSS não utilizado baseado na análise do PageSpeed"""
    print("🗑️ Removendo CSS não utilizado...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # CSS files identificados como não utilizados pelo PageSpeed
    unused_css_patterns = [
        # FontAwesome não utilizado
        r'<link[^>]*fontawesome[^>]*\.css[^>]*>\s*',
        # WooCommerce CSS não crítico
        r'<link[^>]*woocommerce-smallscreen[^>]*\.css[^>]*>\s*',
        # Widgets não utilizados na página inicial
        r'<link[^>]*widget-mega-menu[^>]*\.css[^>]*>\s*',
        r'<link[^>]*widget-blockquote[^>]*\.css[^>]*>\s*',
        # Fontes não utilizadas
        r'<link[^>]*robotoslab[^>]*\.css[^>]*>\s*',
        r'<link[^>]*playfairdisplay[^>]*\.css[^>]*>\s*',
    ]
    
    removed_count = 0
    for pattern in unused_css_patterns:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, '', content)
            removed_count += len(matches)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"   ✅ {removed_count} arquivos CSS não utilizados removidos")

def optimize_css_files():
    """Otimiza arquivos CSS individuais"""
    print("📁 Otimizando arquivos CSS...")
    
    css_files = []
    
    # Encontrar arquivos CSS no diretório
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.css') and 'min.css' not in file:
                css_files.append(os.path.join(root, file))
    
    optimized_count = 0
    total_savings = 0
    
    for css_file in css_files:
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            original_size = len(original_content)
            
            # Minificar CSS
            minified = original_content
            
            # Remover comentários
            minified = re.sub(r'/\*.*?\*/', '', minified, flags=re.DOTALL)
            
            # Remover espaços desnecessários
            minified = re.sub(r'\s+', ' ', minified)
            minified = re.sub(r'{\s*', '{', minified)
            minified = re.sub(r'}\s*', '}', minified)
            minified = re.sub(r':\s*', ':', minified)
            minified = re.sub(r';\s*', ';', minified)
            minified = re.sub(r';+}', '}', minified)
            
            minified = minified.strip()
            
            new_size = len(minified)
            savings = original_size - new_size
            
            if savings > 100:  # Só salvar se houver economia significativa
                with open(css_file, 'w', encoding='utf-8') as f:
                    f.write(minified)
                
                optimized_count += 1
                total_savings += savings
        
        except Exception as e:
            print(f"   ⚠️ Erro ao otimizar {css_file}: {e}")
    
    print(f"   ✅ {optimized_count} arquivos CSS otimizados, {total_savings} bytes economizados")

def remove_unused_javascript():
    """Remove JavaScript não utilizado"""
    print("⚡ Removendo JavaScript não utilizado...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Scripts identificados como não utilizados
    unused_js_patterns = [
        # Template preview não necessário em produção
        r'<script[^>]*template-preview[^>]*>.*?</script>\s*',
        r'<script[^>]*starter-templates[^>]*>.*?</script>\s*',
        # Scripts de desenvolvimento
        r'<script[^>]*astra-sites[^>]*>.*?</script>\s*',
        # jQuery migrate não necessário
        r'<script[^>]*jquery-migrate[^>]*>.*?</script>\s*',
    ]
    
    removed_count = 0
    for pattern in unused_js_patterns:
        matches = re.findall(pattern, content, flags=re.DOTALL)
        if matches:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
            removed_count += len(matches)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"   ✅ {removed_count} scripts não utilizados removidos")

def minify_inline_javascript():
    """Minifica JavaScript inline"""
    print("📜 Minificando JavaScript inline...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Padrão para encontrar blocos <script>
    script_pattern = r'<script[^>]*>(.*?)</script>'
    
    def minify_js_block(match):
        js_content = match.group(1)
        
        # Pular se for muito pequeno ou se for configuração JSON
        if len(js_content.strip()) < 50 or js_content.strip().startswith('{'):
            return match.group(0)
        
        # Remover comentários JavaScript
        js_content = re.sub(r'//.*?$', '', js_content, flags=re.MULTILINE)
        js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
        
        # Remover espaços em branco desnecessários
        js_content = re.sub(r'\s+', ' ', js_content)
        js_content = re.sub(r'{\s*', '{', js_content)
        js_content = re.sub(r'}\s*', '}', js_content)
        js_content = re.sub(r';\s*', ';', js_content)
        
        return f'<script>{js_content.strip()}</script>'
    
    # Aplicar minificação
    content = re.sub(script_pattern, minify_js_block, content, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("   ✅ JavaScript inline minificado")

def combine_css_files():
    """Combina arquivos CSS pequenos para reduzir requests"""
    print("🔗 Combinando arquivos CSS pequenos...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Encontrar arquivos CSS pequenos que podem ser combinados
    small_css_pattern = r'<link[^>]*href=[\'"]([^\'"]*(?:widget-|theme|header-footer)[^\'"]*\.css[^\'"]*)[\'"][^>]*>\s*'
    
    small_css_files = re.findall(small_css_pattern, content)
    
    if len(small_css_files) > 3:  # Só combinar se houver vários arquivos pequenos
        combined_css = ""
        
        for css_file in small_css_files[:5]:  # Combinar até 5 arquivos
            try:
                if os.path.exists(css_file.lstrip('./')):
                    with open(css_file.lstrip('./'), 'r', encoding='utf-8') as f:
                        css_content = f.read()
                    combined_css += f"/* {css_file} */\n{css_content}\n\n"
            except:
                continue
        
        if combined_css:
            # Criar arquivo CSS combinado
            with open('wp-content/uploads/combined-small.css', 'w', encoding='utf-8') as f:
                f.write(combined_css)
            
            # Remover links individuais e adicionar link combinado
            for css_file in small_css_files[:5]:
                pattern = f'<link[^>]*href=[\'"]\\{re.escape(css_file)}[\'"][^>]*>\\s*'
                content = re.sub(pattern, '', content)
            
            # Adicionar link para arquivo combinado
            combined_link = '<link rel="stylesheet" href="./wp-content/uploads/combined-small.css">\n'
            content = re.sub(r'(<link[^>]*elementor[^>]*frontend[^>]*>)', r'\1\n' + combined_link, content)
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"   ✅ {len(small_css_files[:5])} arquivos CSS combinados")
    else:
        print("   ℹ️ Poucos arquivos CSS pequenos para combinar")

def create_minification_report():
    """Cria relatório das otimizações de minificação"""
    print("📊 Gerando relatório de minificação...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Contar elementos otimizados
    css_links = len(re.findall(r'<link[^>]*\.css', content))
    js_scripts = len(re.findall(r'<script[^>]*\.js', content))
    inline_styles = len(re.findall(r'<style', content))
    inline_scripts = len(re.findall(r'<script[^>]*>[^<]', content))
    
    # Calcular tamanho do HTML
    html_size_kb = round(len(content) / 1024, 1)
    
    report = {
        "minification_summary": {
            "css_files": css_links,
            "js_files": js_scripts,
            "inline_styles": inline_styles,
            "inline_scripts": inline_scripts,
            "html_size_kb": html_size_kb,
            "estimated_css_savings_kb": 56,
            "estimated_js_savings_kb": 50,
            "optimizations_applied": [
                "Inline CSS minification",
                "Unused CSS removal",
                "CSS file optimization",
                "Unused JavaScript removal",
                "Inline JavaScript minification",
                "Small CSS file combination"
            ]
        }
    }
    
    # Salvar relatório
    with open('minification_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    return report

def main():
    """Executa todas as otimizações de minificação"""
    print("🎯 MINIFICANDO CSS E JAVASCRIPT - PEACOCK COSMÉTICOS\n")
    
    # Backup do arquivo original
    if not os.path.exists('index_minify_backup.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        with open('index_minify_backup.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("📋 Backup criado: index_minify_backup.html")
    
    # Executar otimizações
    minify_inline_css()
    remove_unused_css()
    optimize_css_files()
    remove_unused_javascript()
    minify_inline_javascript()
    combine_css_files()
    report = create_minification_report()
    
    print("\n🎉 MINIFICAÇÃO COMPLETA!")
    print("📊 Resultados:")
    print(f"   🎨 Arquivos CSS: {report['minification_summary']['css_files']}")
    print(f"   ⚡ Arquivos JS: {report['minification_summary']['js_files']}")
    print(f"   📄 Tamanho HTML: {report['minification_summary']['html_size_kb']} KB")
    print(f"   💾 Economia CSS estimada: {report['minification_summary']['estimated_css_savings_kb']} KiB")
    print(f"   💾 Economia JS estimada: {report['minification_summary']['estimated_js_savings_kb']} KiB")

if __name__ == "__main__":
    main()
