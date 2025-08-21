# Peacock Admin - Sistema de Administração

Sistema de administração React para o site Peacock Cosméticos, com migração completa do WordPress/WooCommerce mantendo 100% de fidelidade visual.

## 🚀 Características

- **React + TypeScript**: Interface moderna e type-safe
- **Autenticação Segura**: JWT tokens com proteção contra ataques
- **Gestão de Conteúdo**: Editor completo para todo o conteúdo do site
- **Preservação Visual**: 100% de fidelidade ao design original
- **WordPress Disguise**: Nenhum rastro do WordPress visível
- **Responsivo**: Funciona perfeitamente em desktop e mobile

## 📋 Pré-requisitos

- Node.js 18+ 
- npm ou yarn
- Git

## 🛠️ Instalação

1. **Clone o repositório**
```bash
git clone <repository-url>
cd peacock-admin
```

2. **Instale as dependências**
```bash
npm install
```

3. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

4. **Instale as dependências do servidor**
```bash
cd server
npm install
cd ..
```

## 🚀 Execução

### Desenvolvimento

1. **Inicie o servidor backend**
```bash
npm run server
```

2. **Inicie o frontend (em outro terminal)**
```bash
npm run dev
```

3. **Acesse a aplicação**
- Frontend: http://localhost:3000
- Admin: http://localhost:3000/admin/login
- API: http://localhost:3001/api

### Produção

1. **Build da aplicação**
```bash
npm run build
```

2. **Inicie o servidor de produção**
```bash
npm start
```

## 🔐 Credenciais de Acesso

**Demonstração:**
- Usuário: `admin`
- Senha: `PeacockAdmin2025!`

⚠️ **IMPORTANTE**: Altere essas credenciais em produção!

## 📁 Estrutura do Projeto

```
peacock-admin/
├── src/
│   ├── components/
│   │   ├── admin/          # Painel administrativo
│   │   ├── auth/           # Autenticação
│   │   ├── frontend/       # Componentes do site
│   │   └── ui/             # Componentes reutilizáveis
│   ├── contexts/           # Contextos React
│   ├── schemas/            # Validação Zod
│   ├── services/           # APIs e serviços
│   └── types/              # Tipos TypeScript
├── server/
│   ├── data/               # Armazenamento JSON
│   ├── uploads/            # Arquivos enviados
│   └── index.js            # Servidor Express
└── public/
    └── assets/             # Assets estáticos
```

## 🎨 Funcionalidades do Admin

### ✅ Implementado
- **Dashboard**: Visão geral e estatísticas
- **SEO & Metadata**: Editor completo de metadados
- **Autenticação**: Login seguro com JWT
- **Gestão de Conteúdo**: API completa para CRUD
- **Validação**: Validação robusta com Zod
- **Upload de Arquivos**: Sistema de upload seguro

### 🚧 Em Desenvolvimento
- **Editor de Empresa**: Dados da empresa
- **Botões de Compra**: Gestão de links de compra
- **Títulos**: Editor de títulos principais
- **Depoimentos**: Gestão de depoimentos
- **FAQ**: Editor de perguntas frequentes
- **Imagens**: Gestão de mídia

## 🔒 Segurança

- **Autenticação JWT**: Tokens seguros com expiração
- **Validação de Entrada**: Sanitização de todos os inputs
- **Proteção CSRF**: Headers de segurança
- **Rate Limiting**: Proteção contra ataques de força bruta
- **Senhas Seguras**: Hash bcrypt com salt
- **Validação de Arquivos**: Tipos e tamanhos controlados

## 🎯 WordPress Disguise

O sistema mantém a estrutura disfarçada do WordPress:
- `wp-content` → `assets`
- `woocommerce` → `ecommerce`
- `elementor` → `page-builder`
- Nenhuma referência ao WordPress visível

## 📱 Responsividade

- **Desktop**: Interface completa do admin
- **Tablet**: Layout adaptado
- **Mobile**: Interface otimizada para toque

## 🔧 Configuração de Produção

1. **Variáveis de Ambiente**
```bash
NODE_ENV=production
JWT_SECRET=your-super-secure-secret
VITE_API_URL=https://your-domain.com/api
```

2. **Servidor Web**
- Configure nginx/Apache para servir os arquivos estáticos
- Configure proxy reverso para a API
- Configure SSL/HTTPS

3. **Banco de Dados** (Opcional)
- Migre de JSON para PostgreSQL/MySQL
- Configure backups automáticos

## 📊 Monitoramento

- **Logs**: Sistema de logging configurável
- **Métricas**: Estatísticas de uso
- **Backups**: Backup automático dos dados
- **Health Check**: Endpoint de verificação

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é propriedade da Peacock Cosméticos.

## 🆘 Suporte

Para suporte técnico:
- Email: sac@peacockcosmeticos.com.br
- Documentação: [Link para docs]

---

**Desenvolvido com ❤️ para Peacock Cosméticos**
