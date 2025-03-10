from crewai import Agent


def get_agents():
    # Agentes executivos especializados nas tarefas de criação de conteúdo para redes sociais
    content_agents = {
        'calendar_agent': Agent(
            role='Especialista em Calendário de Conteúdo',
            goal='Criar um calendário detalhado de postagens para o LinkedIn',
            backstory="Experiente em planejamento de mídia e estratégias de conteúdo, com foco em maximizar engajamento.",
            max_iter=15,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'text_content_agent': Agent(
            role='Criador de Textos',
            goal='Escrever textos engajadores para os conteúdos planejados',
            backstory="Escritor criativo com habilidades em captar a essência da mensagem e adaptá-la para o público-alvo.",
            max_iter=15,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'image_creator_agent': Agent(
            role='Designer Gráfico',
            goal='Criar imagens e visuais para acompanhar os textos dos posts',
            backstory="Designer gráfico com forte senso estético, especializado em criar visuais impactantes para redes sociais.",
            max_iter=15,
            memory=True,            
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'video_scriptwriter_agent': Agent(
            role='Roteirista de Vídeos',
            goal='Elaborar roteiros para vídeos que serão publicados no YouTube',
            backstory="Roteirista experiente, especializado em conteúdo educativo e promocional para plataformas de vídeo.",
            max_iter=15,
            verbose=True,
            memory=True,
            cache=True,
            allow_delegation=True,
        ),
        'data_analytics_agent': Agent(
            role='Analista de Dados de Mídia Social',
            goal='Fornecer análises aprofundadas sobre o desempenho dos posts, identificar tendências e otimizar as estratégias de marketing digital',
            backstory='Especialista em análise de dados com experiência em insights de mídia social, capaz de traduzir dados brutos em estratégias de ação eficazes.',
            max_iter=15,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'customer_engagement_agent': Agent(
            role='Gerente de Engajamento do Cliente',
            goal='Aumentar o engajamento por meio de interações significativas e personalizadas com o público, consolidando a lealdade à marca',
            backstory='Comunicador nato com habilidades em gestão de relacionamento e uma paixão por construir comunidades engajadas em torno de marcas.',
            max_iter=15,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'campaign_strategist': Agent(
            role='Estrategista de Campanha de Google Ads',
            goal='Definir a estratégia de campanha no Google Ads',
            backstory="Especialista em marketing digital com foco em otimização de campanhas de PPC.",
            max_iter=10,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'ad_group_creator': Agent(
            role='Especialista em Criação de Grupos de Anúncios',
            goal='Criar grupos de anúncios eficazes para a campanha',
            backstory="Especialista em SEM com experiência em seleção estratégica de palavras-chave.",
            max_iter=10,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'ad_creator': Agent(
            role='Criador de Anúncios',
            goal='Produzir anúncios persuasivos e conforme as normas do Google Ads',
            backstory="Criativo publicitário especializado em anúncios digitais e copywriting.",
            max_iter=10,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'seo_agent': Agent(
            role='Especialista em SEO',
            goal='Otimizar textos e conteúdos para motores de busca',
            backstory="Especialista em SEO técnico, focado em palavras-chave, links e melhores práticas de otimização.",
            max_iter=10,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'paid_media_manager': Agent(
            role='Gerente de Mídia Paga',
            goal='Criar e gerenciar campanhas de Google Ads e Facebook Ads',
            backstory="Especialista em PPC e estratégias de remarketing, com vasta experiência em campanhas de alto ROI.",
            max_iter=10,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'automation_agent': Agent(
            role='Especialista em Automação de Marketing',
            goal='Automatizar campanhas de marketing e funis de vendas',
            backstory="Especialista em ferramentas de automação como HubSpot, Mailchimp e RD Station.",
            max_iter=15,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'market_research_agent': Agent(
            role='Pesquisador de Mercado',
            goal='Coletar e analisar dados sobre tendências de mercado e concorrentes',
            backstory="Especialista em pesquisa e análise de mercado, ajudando a identificar oportunidades estratégicas.",
            max_iter=12,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        ),
        'influencer_manager': Agent(
            role='Gerente de Relacionamento com Influenciadores',
            goal='Identificar e gerenciar parcerias com influenciadores digitais',
            backstory="Especialista em marketing de influência e construção de relacionamentos de longo prazo.",
            max_iter=10,
            memory=True,
            verbose=True,
            cache=True,
            allow_delegation=True,
        )
    }

    return content_agents