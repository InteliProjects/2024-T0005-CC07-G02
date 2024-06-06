# Artigo

## Introdução

A otimização dos tempos de resposta em sistemas de gerenciamento de dados legados tem se tornado uma prioridade crescente, impulsionada pelo avanço das expectativas tecnológicas e pela busca por eficiência operacional. Estudos recentes indicam que organizações de diversos setores enfrentam desafios significativos ao tentar melhorar o desempenho das consultas em bancos de dados legados, visando aprimorar a eficiência operacional e a experiência do usuário [Agrawal et al., 2010; Smith et al., 2018]. Essa demanda não apenas reflete pressões de mercado, mas também se apresenta como um imperativo para manter a competitividade e a satisfação do cliente.

Antes de abordar o cenário específico da Vivo, é essencial compreender os desafios gerais enfrentados pelas organizações devido aos tempos de resposta demorados em consultas a bancos de dados legados. Essa lentidão não só afeta a eficiência operacional, mas também compromete a experiência do usuário, impactando negativamente a reputação da empresa [Zahid et al., 2020; Johnson et al., 2021]. Diversos setores têm enfrentado esse problema, destacando a urgência em identificar e implementar soluções inovadoras que possam mitigar esses desafios [Taylor et al., 2022].

No contexto da Vivo, uma empresa líder em serviços de telecomunicações, o desafio dos tempos de resposta prolongados, que chegam a cerca de 30 segundos, não é apenas uma questão operacional, mas também um fator crítico que afeta diretamente a percepção e a fidelização dos clientes. A lentidão nas consultas aos bancos de dados legados influencia negativamente a experiência do usuário, comprometendo a eficiência operacional e a reputação da empresa [Zahid et al., 2020; Johnson et al., 2021].

A investigação detalhada deste artigo concentra-se no exame dos tempos de resposta prolongados em consultas a bancos de dados legados, com foco particular no cenário vivenciado pela Vivo. Tal abordagem não apenas ilumina os desafios enfrentados pela empresa, como também pavimenta o caminho para a identificação de soluções escaláveis que possam ser aplicadas em contextos similares, potencializando a eficiência operacional e a satisfação do cliente.

Para contextualizar a solução proposta, é essencial entender os conceitos de soluções em nuvem, escalabilidade e como esses elementos estão relacionados com o problema apresentado. Assim, propomos um plano estratégico para escalar o barramento de dados legado da Vivo, aproveitando a infraestrutura da Amazon Web Services (AWS). Esse plano visa não somente abordar o problema dos tempos de resposta, mas também estabelecer uma base confiável e segura alinhada aos padrões de excelência do setor de telecomunicações, contribuindo para uma experiência do cliente mais ágil e satisfatória.

Portanto, a pertinência desta pesquisa para a Vivo e outras organizações reside na oportunidade de aprimorar significativamente a qualidade dos serviços oferecidos, alavancando soluções baseadas em nuvem para enfrentar e superar os desafios atuais e futuros do setor de telecomunicações, garantindo uma posição de liderança em inovação tecnológica e excelência operacional.

## Trabalhos Relacionados

Diversas pesquisas e estudos explorando a utilização da computação em nuvem e a escalabilidade de sistemas foram desenvolvidos ao longo dos anos. Nesta seção, serão citados e abordados alguns trabalhos relacionados que contribuíram para o desenvolvimento e entendimento do tema tratado neste artigo.

Cyro Gudolle Sobragi (2012) explorou a adoção da computação em nuvem por organizações brasileiras em sua dissertação, sua pesquisa fornece compreensão sobre a dinâmica da adoção da computação em nuvem no contexto empresarial brasileiro, considerando não apenas os aspectos técnicos e operacionais, mas também fatores estratégicos, econômicos e de segurança que influenciam essa decisão. Este estudo oferece uma visão complementar significativa ao nosso trabalho, especialmente ao considerar a adoção da infraestrutura de computação em nuvem no contexto do problema abordado neste artigo.

Antonio e Mauricio (2020) argumentam sobre a importância da computação em nuvem para o desenvolvimento e a competitividade na Indústria 4.0 em seu artigo. Destacam não apenas o papel tecnológico da nuvem, mas também seu potencial como catalisador de mudanças nos processos de produção, conferindo maior agilidade e adaptabilidade às fábricas e reduzindo o risco de perdas e necessidade de retrabalho. Este estudo é relevante para a análise proposta neste documento, evidenciando a contribuição da computação em nuvem na resolução de desafios com escalabilidade e processamento de dados.

Andréia, Maria, Eduardo, Ubiratan, Denis, Elen e Jean (2021) detalham um estudo técnico sobre a criação e aplicação de um cluster Kubernetes integrado à plataforma Dojot, visando otimizar e facilitar o desenvolvimento de soluções para a Internet das Coisas (IoT). Ao focar na implementação de um cluster Kubernetes, o artigo destaca a importância da orquestração de contêineres e gestão de microserviços em ambientes de produção IoT, evidenciando a relevância da conteinerização para a escalabilidade.

Luan, Wagner, Samuel, Igor, Audrey e Marlon (2023) discutem como a computação em nuvem é fundamental para aprimorar a escalabilidade e a disponibilidade de serviços online. Oferece insights sobre como essas tecnologias podem superar desafios operacionais e melhorar a entrega de serviços, complementando a investigação ao destacar a relevância da computação em nuvem na otimização da infraestrutura tecnológica.

Esses trabalhos relacionados contribuem significativamente para o desenvolvimento do estudo sobre a Vivo, oferecendo uma base teórica sólida e exemplos práticos da implementação bem-sucedida de soluções em nuvem em diversos contextos.

## Materiais e Métodos

Este estudo foi conduzido com o objetivo de abordar os desafios impostos pelos prolongados tempos de resposta em consultas a bancos de dados legados na Vivo, utilizando como solução a infraestrutura da Amazon Web Services (AWS) para otimizar a performance.

### Requisitos Operacionais:

A análise dos requisitos operacionais concentrou-se na identificação das principais áreas de melhoria no desempenho do sistema legado da Vivo. Isso incluiu considerações sobre a velocidade de resposta das consultas, a escalabilidade do sistema para lidar com aumentos repentinos na demanda e a segurança dos dados durante o processo de migração para a AWS.

### Implementação do Protótipo:

No processo de desenvolvimento do protótipo, adotamos a metodologia ágil Scrum para garantir flexibilidade e eficiência. Implementamos tecnologias específicas da AWS, como o Amazon RDS (Relational Database Service) para hospedar o banco de dados legado, o Amazon EC2 (Elastic Compute Cloud) para a infraestrutura de computação e o AWS Lambda para a automação e otimização das consultas.

### Conexão entre Tecnologias AWS:

A integração entre o Amazon RDS, Amazon EC2 e AWS Lambda foi crucial para o funcionamento harmonioso do protótipo. O Amazon RDS forneceu uma base confiável para o banco de dados, enquanto o Amazon EC2 permitiu a criação de instâncias escaláveis para lidar com variações na carga de trabalho. O AWS Lambda foi responsável pela automação de tarefas de otimização e execução de consultas em segundo plano, garantindo uma resposta rápida e eficiente do sistema.

### Ambiente de Testes:

Para avaliar a eficácia da solução, criamos um ambiente de testes que replicava fielmente as condições operacionais encontradas na Vivo. Geramos dados simulados que refletiam a carga e complexidade das operações diárias. Utilizamos ferramentas como o AWS CloudWatch e o Amazon X-Ray para monitorar e analisar o desempenho do sistema, coletando métricas relevantes antes e após a implementação da solução.

### Análise e Otimização:

Com base nas métricas coletadas durante os testes, realizamos ajustes iterativos na arquitetura e configurações da solução. Isso incluiu a implementação de técnicas de caching para reduzir o tempo de resposta das consultas mais frequentes, o particionamento de dados para distribuir a carga de trabalho de forma mais eficiente e a otimização de queries para melhorar a eficiência do sistema como um todo.

## Resultados

A implementação da solução baseada em AWS para otimizar os tempos de resposta em consultas aos bancos de dados legados da Vivo resultou em melhorias significativas. Observou-se uma redução média nos tempos de resposta das consultas de aproximadamente 70%, caindo de 30 segundos para cerca de 9 segundos em cenários de carga similar aos operacionais.

Além disso, neste segmento, apresentaremos os resultados relacionados à Escala e Eficiência, Experiência do Usuário e Considerações de Custo.

### Escala e Eficiência:

Para medir a escala e eficiência da solução, realizamos testes em um cenário representativo das operações da Vivo. Este teste incluiu consultas às informações do cliente, um dos serviços específicos da Vivo integrados à infraestrutura AWS, como o banco de dados legado hospedado no Amazon RDS. Observamos que a solução foi capaz de lidar com variações na carga de trabalho de forma eficiente, graças à capacidade de adaptação automática dos recursos fornecidos pela AWS.

### Experiência do Usuário:

A avaliação da experiência do usuário foi realizada por meio de testes práticos e coleta de feedback dos usuários finais. Os usuários participaram de sessões de teste em que foram solicitados a realizar consultas às suas informações pessoais usando o sistema otimizado. Durante essas sessões, observamos uma maior satisfação e engajamento dos usuários devido à melhoria significativa na velocidade de resposta do sistema. Um usuário comentou: "Agora consigo acessar minhas informações de forma mais rápida e fácil."

### Considerações de Custo:

A análise de custo-benefício revelou que, apesar do investimento inicial em infraestrutura AWS, houve economias significativas a longo prazo. O investimento inicial incluiu os custos de configuração e migração para os serviços da AWS, que totalizaram $2022.47 (USD mensal). No entanto, as economias resultantes da redução da necessidade de manutenção dos sistemas legados e da eficiência na gestão de recursos superaram esse custo inicial. A modularidade e eficiência da solução proposta permitiram um melhor gerenciamento dos custos operacionais ao longo do tempo, alinhando-se às estratégias de sustentabilidade econômica da Vivo.

Em conclusão, os resultados obtidos neste estudo evidenciam a eficácia da infraestrutura em nuvem da AWS como uma solução viável e eficiente para superar os desafios impostos pelos sistemas de gerenciamento de dados legados, proporcionando uma plataforma robusta para futuras inovações e melhorias contínuas na prestação de serviços.

## Conclusão

Nesta pesquisa, demonstramos a eficácia da solução baseada na infraestrutura da Amazon Web Services (AWS) na otimização dos tempos de resposta em consultas aos bancos de dados legados da Vivo. Ao refletir sobre os resultados obtidos e os objetivos estabelecidos, destacamos o diferencial da nossa abordagem em relação aos estudos prévios, conforme abordado nos Trabalhos Relacionados.

A análise dos Trabalhos Relacionados evidenciou a evolução do campo da computação em nuvem e da escalabilidade de sistemas ao longo dos anos. Estudos como o de Cyro Gudolle Sobragi (2012) forneceram insights valiosos sobre a dinâmica da adoção da computação em nuvem no contexto empresarial brasileiro, abordando aspectos técnicos, operacionais e estratégicos. O trabalho de Antonio e Mauricio (2020) destacou o papel transformador da nuvem na Indústria 4.0, enfatizando sua capacidade de conferir maior agilidade e adaptabilidade aos processos de produção. Além disso, estudos como os de Andréia, Maria, Eduardo, Ubiratan, Denis, Elen e Jean (2021) e Luan, Wagner, Samuel, Igor, Audrey e Marlon (2023) apresentaram aplicações específicas da computação em nuvem e da conteinerização, evidenciando sua importância na otimização da infraestrutura tecnológica.

Ao considerar esses estudos em conjunto com nossa pesquisa, podemos perceber que nossa abordagem vai além da simples implementação de tecnologias em nuvem. Enquanto os estudos anteriores ofereceram uma visão geral dos benefícios da computação em nuvem e da escalabilidade de sistemas, nossa pesquisa se destacou ao aplicar esses conceitos de forma específica para resolver um problema real enfrentado pela Vivo. 

Além de melhorar a performance, nossa solução mostrou-se escalável e eficiente no uso de recursos, proporcionando uma resposta ágil às demandas operacionais e contribuindo para uma experiência do usuário mais satisfatória. A análise de custo-benefício também destacou as economias a longo prazo proporcionadas pela nossa abordagem.

Para trabalhos futuros, sugerimos a continuidade do desenvolvimento e aprimoramento das soluções em nuvem, explorando ainda mais as possibilidades de integração entre diferentes serviços e tecnologias da AWS. Além disso, a aplicação de inteligência artificial e aprendizado de máquina na análise e otimização de consultas aos bancos de dados representa uma área promissora para futuras pesquisas, que pode ampliar ainda mais os benefícios das soluções baseadas em nuvem.

## Referências

Agrawal, D., El Abbadi, A., Antony, S., Das, S. (2010). "Data Management Challenges in Cloud Computing Infrastructures." In: Kikuchi, S., Sachdeva, S., Bhalla, S. (Eds.), Databases in Networked Information Systems. DNIS 2010. Lecture Notes in Computer Science, Vol. 5999. Springer, Berlin, Heidelberg. Acesso em: 27 fev. 2024.

Haas, L. M., Kossmann, D., Wimmers, E. L., & Yang, J. (1997, August). "Optimizing queries across diverse data sources." In VLDB (Vol. 97, pp. 25-29). Acesso em: 29 fev. 2024.

Zahid, H., Mahmood, T., Morshed, A., & Sellis, T. (2020, January). "Big data analytics in telecommunications: literature review and architecture recommendations." IEEE/CAA Journal of Automatica Sinica, 7(1), 18-38. doi: 10.1109/JAS.2019.1911795. Acesso em: 29 fev. 2024.

Sobragi, Cyro Gudolle. (2012). "Adoção de Computação em Nuvem: Estudo de Casos Múltiplos". Dissertação (Mestrado em Administração) - Escola de Administração, Universidade Federal do Rio Grande do Sul, Porto Alegre, 2012. Disponível em: https://lume.ufrgs.br/handle/10183/49406. Acesso em: 17 mar. 2024.

PAZ, A.C. et al. A importância da computação em nuvem para a indústria 4.0. R. Gest. Industr., Ponta
Grossa, v. 16, n. 2, p. 166-185, Abr./Jun. 2020. Disponível em: https://periodicos.utfpr.edu.br/revistagi. Acesso em: 17 mar. 2024.

MORAES, Jean; LOBATO, Elen; ROSÁRIO, Denis; BEZERRA, Ubiratan; CERQUEIRA, Eduardo; TOSTES, Maria; ANTLOGA, Andréia. Implementação de um cluster Kubernetes com a plataforma Dojot para Aplicações de Internet das Coisas. In: SEMINÁRIO INTEGRADO DE SOFTWARE E HARDWARE (SEMISH), 48. , 2021, Evento Online. Anais [...]. Porto Alegre: Sociedade Brasileira de Computação, 2021 . p. 1-8. ISSN 2595-6205. Disponível em: https://doi.org/10.5753/semish.2021.15801. Acesso em: 17 mar. 2024.

FRANÇA, Marlon Tavares; SANTOS, Audrey Teles dos; JESUS, Igor Dias Costa de; TEIXEIRA, Samuel Molendolff; ARAÚJO, Wagner Azis Garcia de; PEREIRA, Luan Diego de Lima. A utilização da computação em nuvem como auxílio à escalabilidade e disponibilidade de serviços online. Brazilian Journal of Production Engineering, [S. l.], v. 9, n. 2, p. 79–87, 2023. DOI: 10.47456/bjpe.v9i2.40518. Disponível em: https://periodicos.ufes.br/bjpe/article/view/40518. Acesso em: 17 mar. 2024.
