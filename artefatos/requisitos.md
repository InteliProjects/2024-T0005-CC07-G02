# Requisitos Funcionais e Não Funcionais

### Requisitos Funcionais

**RF1:** Cadastro de Cliente
- Permitir que novos clientes se cadastrem no sistema, fornecendo informações detalhadas, como nome, endereço, número de telefone, e-mail, forma de pagamento, entre outros.

**RF2:** Consulta de Fatura
- Permitir que os clientes consultem suas faturas recentes de serviços contratados, apresentando detalhes específicos, como serviços utilizados, datas de uso, valores individuais, e total a ser pago.

**RF3:** Acesso à Internet Residencial e Empresarial
- Permitir que os clientes consultem seus serviços de acesso à internet residencial e empresarial, especificando velocidades de conexão, planos disponíveis e opções de upgrades.

**RF4:** Telefonia Fixa e Móvel
- Permitir que os clientes consultem seus serviços de telefonia fixa e móvel, incluindo opções de pacotes, minutos incluídos, e detalhes sobre chamadas internacionais, se aplicável.

**RF5:** Outros Produtos e Serviços (TV e Streaming)
- Permitir que os clientes consultem seus serviços adicionais, como TV por assinatura e serviços de streaming, com detalhes sobre canais, pacotes de entretenimento, e opções de conteúdo disponíveis.

### Requisitos Não Funcionais

**RNF1:** Adequação Funcional<br>
**Descrição:** O sistema deve atender às necessidades específicas e requisitos funcionais do usuário, proporcionando funcionalidades relevantes para o contexto da Vivo.<br>
**Métrica:** 100% de aderência aos requisitos funcionais estabelecidos no documento de especificação.<br>
**Plano de Teste:** Será realizado um teste de validação funcional, verificando se todas as funcionalidades atendem às expectativas e requisitos do cliente.

**RNF2:** Eficiência de Performance<br>
**Descrição:** O sistema deve executar as operações de forma eficiente, garantindo um tempo de resposta rápido para as consultas no banco de dados.<br>
**Métrica:** O tempo de resposta para consultas no banco de dados deve ser inferior a 2 segundos em condições normais de carga.<br>
**Plano de Teste:** Testes de desempenho serão conduzidos para avaliar a eficiência do sistema em diferentes cenários de carga, garantindo que os tempos de resposta estejam dentro dos limites estabelecidos.

**RNF3:** Compatibilidade<br>
**Descrição:** O sistema deve ser compatível com diferentes navegadores, dispositivos e sistemas operacionais, assegurando uma experiência consistente para os usuários.<br>
**Métrica:** O sistema deve funcionar corretamente nas versões mais recentes dos principais navegadores (Chrome, Edge, Safari) e em dispositivos móveis (iOS e Android).<br>
**Plano de Teste:** Será realizado um teste de compatibilidade em diferentes ambientes para garantir que o sistema funcione corretamente em diversas configurações.

**RNF4:** Usabilidade<br>
**Descrição:** O sistema deve ser de fácil utilização, com uma interface intuitiva e amigável para o usuário final.<br>
**Métrica:** 80% ou mais dos usuários de teste devem completar tarefas designadas sem assistência adicional, indicando uma boa usabilidade.<br>
**Plano de Teste:** Testes de usabilidade serão conduzidos com usuários representativos para avaliar a facilidade de navegação e compreensão do sistema.

**RNF5:** Confiabilidade<br>
**Descrição:** O sistema deve ser confiável, minimizando o número de falhas e garantindo a consistência e integridade dos dados.<br>
**Métrica:** O sistema deve ter uma taxa de disponibilidade de 99,9% ou superior, indicando alta confiabilidade.<br>
**Plano de Teste:** Testes de confiabilidade serão realizados, simulando situações de falha e verificando a capacidade do sistema em se recuperar sem perda de dados.

**RNF6:** Segurança<br>
**Descrição:** O sistema deve garantir a segurança dos dados, implementando medidas de proteção contra acesso não autorizado e ameaças cibernéticas.<br>
**Métrica:** O sistema deve passar por testes de penetração e auditorias de segurança, sem identificação de vulnerabilidades críticas.<br>
**Plano de Teste:** Testes de segurança serão conduzidos para identificar possíveis vulnerabilidades e avaliar a eficácia das medidas de segurança implementadas.

**RNF7:** Manutenibilidade<br>
**Descrição:** O sistema deve ser de fácil manutenção, permitindo a introdução de atualizações e correções de forma eficiente.<br>
**Métrica:** O tempo médio para implementar uma atualização de software não deve exceder 4 horas.<br>
**Plano de Teste:** Testes de manutenibilidade serão realizados para avaliar a facilidade com que as atualizações podem ser implementadas sem impactar negativamente o sistema.

**RNF8:** Portabilidade<br>
**Descrição:** O sistema deve ser facilmente adaptável a diferentes ambientes e plataformas, garantindo flexibilidade e portabilidade.<br>
**Métrica:** O sistema deve funcionar corretamente em pelo menos três configurações de hardware e software diferentes.<br>
**Plano de Teste:** Testes de portabilidade serão conduzidos para verificar a capacidade do sistema em funcionar corretamente em diferentes configurações de hardware e software.
