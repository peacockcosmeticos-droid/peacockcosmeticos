#!/usr/bin/env python3
"""
PEACOCK COSMÉTICOS - IMPLEMENTAÇÃO DE LAZY LOADING
Configura carregamento tardio para imagens e vídeos fora da tela (economia de 325 KiB)
"""

import re
import os

def implement_image_lazy_loading():
    """Implementa lazy loading para imagens fora da tela"""
    print("🖼️ Implementando lazy loading para imagens...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Imagens críticas que devem carregar imediatamente (above-the-fold)
    critical_images = [
        'banner01.jpg',
        'banner03.jpg', 
        'peecock-08.png',
        'selo-aprovado-anvisa',
        'dermatologicamente.png'
    ]
    
    # Padrão para encontrar tags img
    img_pattern = r'<img([^>]*?)src="([^"]*)"([^>]*?)>'
    
    def replace_img(match):
        before_src = match.group(1)
        src = match.group(2)
        after_src = match.group(3)
        
        # Pular se já tem loading attribute
        if 'loading=' in before_src + after_src:
            return match.group(0)
        
        # Pular imagens críticas
        if any(critical in src for critical in critical_images):
            return match.group(0)
        
        # Adicionar lazy loading para imagens não críticas
        return f'<img{before_src}src="{src}" loading="lazy" decoding="async"{after_src}>'
    
    # Aplicar lazy loading
    content = re.sub(img_pattern, replace_img, content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Contar imagens com lazy loading
    lazy_images = len(re.findall(r'loading="lazy"', content))
    print(f"   ✅ {lazy_images} imagens configuradas com lazy loading")

def implement_video_lazy_loading():
    """Implementa lazy loading para vídeos"""
    print("🎥 Implementando lazy loading para vídeos...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Padrão para encontrar tags video
    video_pattern = r'<video([^>]*?)>'
    
    def optimize_video(match):
        video_attrs = match.group(1)
        
        # Adicionar atributos de otimização se não existirem
        optimizations = []
        
        if 'preload=' not in video_attrs:
            optimizations.append('preload="none"')
        
        if 'loading=' not in video_attrs:
            optimizations.append('loading="lazy"')
            
        if optimizations:
            return f'<video{video_attrs} {" ".join(optimizations)}>'
        
        return match.group(0)
    
    # Aplicar otimizações de vídeo
    content = re.sub(video_pattern, optimize_video, content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Contar vídeos otimizados
    lazy_videos = len(re.findall(r'loading="lazy".*?<video', content))
    print(f"   ✅ {lazy_videos} vídeos configurados com lazy loading")

def add_intersection_observer():
    """Adiciona Intersection Observer para lazy loading avançado"""
    print("👁️ Adicionando Intersection Observer...")
    
    intersection_script = """
<script>
// Advanced Lazy Loading with Intersection Observer
(function() {
    // Check if Intersection Observer is supported
    if ('IntersectionObserver' in window) {
        
        // Lazy load images
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        img.classList.add('loaded');
                        observer.unobserve(img);
                    }
                }
            });
        }, {
            rootMargin: '50px 0px',
            threshold: 0.01
        });
        
        // Observe all lazy images
        document.querySelectorAll('img[loading="lazy"]').forEach(img => {
            img.classList.add('lazy');
            imageObserver.observe(img);
        });
        
        // Lazy load videos
        const videoObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const video = entry.target;
                    if (video.dataset.src) {
                        video.src = video.dataset.src;
                        video.load();
                        observer.unobserve(video);
                    }
                }
            });
        }, {
            rootMargin: '100px 0px',
            threshold: 0.01
        });
        
        // Observe all lazy videos
        document.querySelectorAll('video[loading="lazy"]').forEach(video => {
            videoObserver.observe(video);
        });
        
        // Lazy load background images
        const bgObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const element = entry.target;
                    if (element.dataset.bg) {
                        element.style.backgroundImage = `url(${element.dataset.bg})`;
                        element.classList.add('bg-loaded');
                        observer.unobserve(element);
                    }
                }
            });
        });
        
        // Observe elements with data-bg attribute
        document.querySelectorAll('[data-bg]').forEach(el => {
            bgObserver.observe(el);
        });
    }
})();
</script>
"""
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Adicionar script antes do fechamento do body
    content = re.sub(r'</body>', intersection_script + '</body>', content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("   ✅ Intersection Observer adicionado")

def add_lazy_loading_css():
    """Adiciona CSS para lazy loading"""
    print("🎨 Adicionando CSS para lazy loading...")
    
    lazy_css = """
<style>
/* Lazy Loading Styles */
img.lazy {
    opacity: 0;
    transition: opacity 0.3s ease;
}

img.loaded {
    opacity: 1;
}

/* Placeholder for lazy images */
img[loading="lazy"] {
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: loading 1.5s infinite;
}

@keyframes loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

img.loaded {
    background: none;
    animation: none;
}

/* Video lazy loading */
video[loading="lazy"] {
    background: #f5f5f5;
    border: 1px solid #ddd;
}

/* Background image lazy loading */
[data-bg] {
    background-color: #f5f5f5;
    transition: background-image 0.3s ease;
}

.bg-loaded {
    background-color: transparent;
}
</style>
"""
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Adicionar CSS antes do fechamento do head
    content = re.sub(r'</head>', lazy_css + '</head>', content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("   ✅ CSS para lazy loading adicionado")

def optimize_background_images():
    """Otimiza imagens de background para lazy loading"""
    print("🖼️ Otimizando imagens de background...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Encontrar elementos com background-image inline
    bg_pattern = r'style="([^"]*background-image:\s*url\([\'"]?([^\'")]+)[\'"]?\)[^"]*)"'
    
    def optimize_bg(match):
        full_style = match.group(1)
        bg_url = match.group(2)
        
        # Remover background-image do style e adicionar data-bg
        new_style = re.sub(r'background-image:\s*url\([\'"]?[^\'")]+[\'"]?\);?', '', full_style)
        new_style = new_style.strip().rstrip(';')
        
        if new_style:
            return f'style="{new_style}" data-bg="{bg_url}"'
        else:
            return f'data-bg="{bg_url}"'
    
    # Aplicar otimização
    content = re.sub(bg_pattern, optimize_bg, content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Contar backgrounds otimizados
    bg_count = len(re.findall(r'data-bg=', content))
    print(f"   ✅ {bg_count} imagens de background otimizadas")

def create_lazy_loading_report():
    """Cria relatório das otimizações de lazy loading"""
    print("📊 Gerando relatório de lazy loading...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Contar elementos otimizados
    lazy_images = len(re.findall(r'loading="lazy".*?<img', content))
    lazy_videos = len(re.findall(r'loading="lazy".*?<video', content))
    bg_images = len(re.findall(r'data-bg=', content))
    total_images = len(re.findall(r'<img', content))
    
    report = {
        "lazy_loading_summary": {
            "lazy_images": lazy_images,
            "total_images": total_images,
            "lazy_percentage": round((lazy_images / total_images * 100), 1) if total_images > 0 else 0,
            "lazy_videos": lazy_videos,
            "background_images": bg_images,
            "estimated_savings_kb": 325,
            "optimizations_applied": [
                "Native lazy loading for images",
                "Video preload optimization", 
                "Intersection Observer implementation",
                "Background image lazy loading",
                "Loading placeholders with CSS"
            ]
        }
    }
    
    # Salvar relatório
    with open('lazy_loading_report.json', 'w', encoding='utf-8') as f:
        import json
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    return report

def main():
    """Executa todas as implementações de lazy loading"""
    print("🎯 IMPLEMENTANDO LAZY LOADING - PEACOCK COSMÉTICOS\n")
    
    # Backup do arquivo original
    if not os.path.exists('index_lazy_backup.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        with open('index_lazy_backup.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("📋 Backup criado: index_lazy_backup.html")
    
    # Executar implementações
    implement_image_lazy_loading()
    implement_video_lazy_loading()
    add_intersection_observer()
    add_lazy_loading_css()
    optimize_background_images()
    report = create_lazy_loading_report()
    
    print("\n🎉 LAZY LOADING IMPLEMENTADO!")
    print("📊 Resultados:")
    print(f"   🖼️ Imagens com lazy loading: {report['lazy_loading_summary']['lazy_images']}")
    print(f"   📹 Vídeos otimizados: {report['lazy_loading_summary']['lazy_videos']}")
    print(f"   🎨 Backgrounds otimizados: {report['lazy_loading_summary']['background_images']}")
    print(f"   📈 Porcentagem de imagens lazy: {report['lazy_loading_summary']['lazy_percentage']}%")
    print(f"   💾 Economia estimada: {report['lazy_loading_summary']['estimated_savings_kb']} KiB")

if __name__ == "__main__":
    main()
