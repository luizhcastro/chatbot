# Chatbot HEMOBA

Este é um projeto acadêmico onde foi criado um chatbot para responder perguntas relacionadas ao HEMOBA (Hemocentro de Vitória da Conquista). Ele fornece informações sobre localização, horários de funcionamento, requisitos para doação de sangue, como acessar resultados de exames e documentos necessários para doação.

## Requisitos
Antes de executar o chatbot, verifique se você possui os seguintes itens instalados:

- Python 3.7 (é necessário ser a versão 3.7 por motivos de compatibilidade com os requisitos apresentados no requirements.txt)
- Gerenciador de pacotes `pip`

## Instalação

1. Instale as dependências necessárias:
   ```terminal
   pip install -r requirements.txt
   ```

## Como Executar
1. Inicie o chatbot:
   ```terminal
   python robo.py
   ```
2. Realize o treinamento:
   ```terminal
   python treinamento.py
   ```
3. Inicie o serviço:
   ```terminal
   python servico.py
   ```
4. Acesse o navegador web:
   http://localhost:5000/resposta/*<escreva_sua_mensagem_aqui>*
## Exemplo de Uso
Quando iniciado, o chatbot pode responder perguntas como:

- "Onde fica o HEMOBA?"
- "Qual o horário de funcionamento?"
- "Quem pode doar sangue?"

O chatbot irá fornecer respostas baseadas no corpus configurado.
