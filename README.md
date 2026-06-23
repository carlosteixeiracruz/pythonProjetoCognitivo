# Arquitetura Híbrida de LLM & Grafos de Conhecimento com NetworkX para Auxílio Cognitivo

> Orquestração Dinâmica de Modelos de Linguagem e Engenharia de Contexto Interseccional.

---

## 🧠 Sobre o Projeto
O **EcoCognição** é um ecossistema de suporte cognitivo e de saúde mental projetado para o ambiente educacional e corporativo. Diferente de soluções que utilizam modelos de linguagem puros (LLMs) de forma isolada — os quais são suscetíveis a alucinações, perda de memória contextual e ausência de travas éticas —, esta solução adota uma **Arquitetura Híbrida**.

O sistema separa a **lógica conceitual e científica** da **geração de texto**:
1. **NetworkX (Camada de Grafo):** Atua como o "Cérebro Clínico/Pedagógico", mapeando o estado do usuário e ditando diretrizes científicas rígidas e protocolos éticos.
2. **Marcadores Sociais:** Camada que contextualiza o indivíduo através de recortes interseccionais (idade, identidade de gênero, etnia) para calibração de empatia sem estereótipos.
3. **Google Gemini (LLM):** Atua estritamente como a "Voz Humana", construindo respostas fluidas e dinâmicas, mas sempre guiada pelas regras injetadas pelo Grafo. 

---

## 🛡️ Protocolos Críticos e Resiliência

* **Protocolo de Emergência Ética (Crise):** Caso o sistema detecte termos associados a abuso, violência doméstica ou risco iminente, o Grafo do `NetworkX` intercepta o fluxo gerativo comum imediatamente, assumindo o controle para disparar respostas protetivas e exibir canais oficiais de denúncia do Governo Federal (Disque 100 / Disque 180).
* **Motor Local de Contingência (Anti-Crash):** Se houver falha de rede ou estouro na cota de requisições da API (`Erro 429 Resource Exhausted`), o motor de processamento local baseado em NLP assume a operação de forma transparente para que o usuário nunca fique desamparado.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.14+**
* **NetworkX** (Engenharia de Grafos de Conhecimento)
* **Google GenAI SDK** (Integração com Gemini 2.5)
* **Tkinter** (Interface Gráfica assíncrona baseada em Threads)

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o Python instalado e as dependências necessárias:
```bash
   pip install networkx google-genai