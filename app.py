import tkinter as tk
from tkinter import ttk
import networkx as nx
from datetime import datetime
import threading

try:
    from google import genai
    from google.genai import types
    GEMINI_DISPONIVEL = True
except ImportError:
    GEMINI_DISPONIVEL = False

# =====================================================================
# 1. ARQUITETURA DO GRAFO COGNITIVO COM PROTOCOLO DE CRISE (NetworkX)
# =====================================================================
grafo_cognitivo = nx.DiGraph()
grafo_cognitivo.add_node("RAIVA", diretriz="Valide a frustração imediatamente. Redirecione o foco para um desafio mecânico sutil.")
grafo_cognitivo.add_node("TRISTEZA", diretriz="Demonstre alta empatia e acolhimento. Reduza a exigência cognitiva. Sugira pausa reflexiva.")
grafo_cognitivo.add_node("FRUSTRACAO", diretriz="Fracione o problema em etapas simples. Foque em micro-vitórias.")
grafo_cognitivo.add_node("NEUTRO", diretriz="Mantenha diálogo de acolhimento padrão. Incentive o usuário a se aprofundar.")

# NOVO: Nó de Segurança Crítica
grafo_cognitivo.add_node("CRISE_SEGURANCA", diretriz="EMERGÊNCIA ÉTICA: O usuário relatou violência física, abuso ou perigo iminente. Interrompa abordagens pedagógicas. Seja estritamente protetivo, empático e forneça canais oficiais de ajuda urgentemente (Disque 100 / Disque 180).")

# Memória global de conversa mantida na sessão
historico_conversa = []

# =====================================================================
# 2. MOTOR COGNITIVO COM MEMÓRIA E FILTRO DE SEGURANÇA
# =====================================================================
def processar_interacao(desabafo, perfil, api_key_usuario=None):
    global historico_conversa
    texto_min = desabafo.lower()
    
    # Gatilhos de Segurança Crítica (Prioridade Máxima)
    gatilhos_crise = ["apanhando", "apanhar", "surra", "bateram", "me bate", "violência", "agredido", "agressão", "abuso"]
    gatilhos_raiva = ["raiva", "odeio", "quebrar", "revolta", "pessimo", "ódio", "inferno"]
    gatilhos_tristeza = ["triste", "cansado", "cansaddo", "desistir", "mal", "esgotado", "tristeza", "chateado", "chorar", "desanimado"]
    gatilhos_frustracao = ["tentando", "não consigo", "difícil", "travei", "erro", "frustrado", "bloqueado", "contas", "dívida", "dinheiro", "atrasar"]

    # Classificação hierárquica por prioridade
    if any(palavra in texto_min for palavra in gatilhos_crise):
        no_ativo = "CRISE_SEGURANCA"
    elif any(palavra in texto_min for palavra in gatilhos_raiva):
        no_ativo = "RAIVA"
    elif any(palavra in texto_min for palavra in gatilhos_tristeza):
        no_ativo = "TRISTEZA"
    elif any(palavra in texto_min for palavra in gatilhos_frustracao):
        no_ativo = "FRUSTRACAO"
    else:
        no_ativo = "NEUTRO"

    diretriz = grafo_cognitivo.nodes[no_ativo]["diretriz"]
    
    try:
        ano_nascimento = int(perfil['nascimento'].split('/')[-1])
        idade = datetime.now().year - ano_nascimento
    except:
        idade = 16
        
    # Adiciona a mensagem atual ao histórico da sessão
    historico_conversa.append(f"Usuário: {desabafo}")
    if len(historico_conversa) > 6:  # Mantém as últimas 6 interações para dar contexto
        historico_conversa.pop(0)
        
    contexto_passado = "\n".join(historico_conversa[:-1])

    # 2.1 INTEGRAÇÃO COM IA REAL (COM MEMÓRIA CONTEXTUAL)
    if GEMINI_DISPONIVEL and api_key_usuario:
        try:
            prompt_sistema = f"""
            Você é um assistente de suporte cognitivo e emocional de elite baseado em IA Híbrida.
            
            PERFIL DO USUÁRIO:
            - Identidade: Pessoa de etnia {perfil['etnia']}, gênero {perfil['genero']}, com {idade} anos.
            
            DIRETRIZ CRÍTICA DO GRAFO (OBRIGATÓRIO SEGUIR): {diretriz}
            
            HISTÓRICO DA CONVERSA PARA CONTEXTO:
            {contexto_passado}
            
            REGRAS DE TOM DE VOZ:
            1. Use o histórico para responder de forma coerente a perguntas como "por que você disse isso?".
            2. Nunca liste os dados do perfil abertamente ("Como você tem X anos..."). Transforme em empatia sutil.
            3. Se o Nó for CRISE_SEGURANCA, concentre-se inteiramente em apoiar a integridade física da pessoa e informe os números de ajuda do Brasil (Disque 100 / 180).
            """
            
            client_ai = genai.Client(api_key=api_key_usuario)
            response = client_ai.models.generate_content(
                model='gemini-2.5-flash',
                contents=desabafo,
                config=types.GenerateContentConfig(
                    system_instruction=prompt_sistema,
                    temperature=0.7
                )
            )
            
            resposta_texto = response.text.strip()
            historico_conversa.append(f"IA: {resposta_texto}")
            
            return (
                f"📍 [NetworkX Node]: {no_ativo}\n"
                f"🎯 [Strategy]: {diretriz}\n"
                f"{'-'*80}\n"
                f"🤖 IA Orquestrada:\n"
                f"\"{resposta_texto}\"\n"
            )
        except Exception as e:
            print(f"Erro na API: {e}. Mudando para modo offline.")

    # 2.2 MOTOR LOCAL DE CONTINGÊNCIA (Variado e Seguro para Crises)
    if no_ativo == "CRISE_SEGURANCA":
        texto_ia = "Sinto muito que você esteja passando por isso. Situações de violência física dentro de casa são inaceitáveis e perigosas. Por favor, saiba que você não está só e existem redes de proteção. Você pode ligar de forma anônima e gratuita para o Disque 100 (Direitos Humanos) ou Disque 180 (Orientação de Defesa da Mulher) para receber ajuda especializada e proteção imediata."
    elif no_ativo == "RAIVA":
        texto_ia = "Compreendo perfeitamente o seu desabafo. Quando o estresse acumulado transborda, focar na mesma tarefa só aumenta a tensão. O que acha de darmos uma quebra de padrão de 2 minutos com um desafio rápido de lógica?"
    elif no_ativo == "TRISTEZA":
        texto_ia = "Sei que esse momento de exaustão e desânimo parece insustentável. É legítimo sentir cansaço quando nos falta apoio e os prazos apertam. Recomendo fortemente uma pausa intencional agora para restabelecer suas energias."
    elif no_ativo == "FRUSTRACAO":
        texto_ia = "Trancar o progresso ou lidar com incertezas financeiras gera um forte bloqueio. Vamos fracionar esse problema? Se pudermos focar em apenas uma micro-vitória simples hoje, qual seria?"
    else:
        texto_ia = "Entendo o que trouxe. Estou te ouvindo atentamente para te ajudar a organizar as ideias. O que mais tem passado pela sua cabeça sobre isso?"

    historico_conversa.append(f"IA: {texto_ia}")
    
    return (
        f"📍 [NetworkX Node]: {no_ativo}\n"
        f"🎯 [Strategy]: {diretriz}\n"
        f"{'-'*80}\n"
        f"🤖 IA Customizada (Modo Resiliência Local):\n"
        f"Contexto Ativo: {idade} anos | Gênero: {perfil['genero']} | Identidade: {perfil['etnia']}\n\n"
        f"\"{texto_ia}\"\n"
    )

# =====================================================================
# 3. INTERFACE GRÁFICA (Tkinter)
# =====================================================================
def executar_processamento_em_segundo_plano(msg, perfil, api_key):
    botao_enviar.config(state=tk.DISABLED, text="Processando...")
    resposta_ia = processar_interacao(msg, perfil, api_key)
    
    area_chat.config(state=tk.NORMAL)
    area_chat.insert(tk.END, f"{resposta_ia}\n", "ia")
    area_chat.insert(tk.END, f"{'='*75}\n\n")
    area_chat.config(state=tk.DISABLED)
    area_chat.see(tk.END)
    
    botao_enviar.config(state=tk.NORMAL, text="Enviar")

def iniciar_envio():
    msg = entrada_chat.get().strip()
    if not msg: return
    
    perfil = {
        "nascimento": entrada_nascimento.get(),
        "genero": combo_genero.get(),
        "etnia": combo_etnia.get()
    }
    
    api_key = entrada_api_key.get().strip()
    if api_key in ["Insira sua Gemini API Key aqui (Opcional)", ""]: api_key = None
    
    area_chat.config(state=tk.NORMAL)
    area_chat.insert(tk.END, f"Você: {msg}\n\n", "usuario")
    area_chat.config(state=tk.DISABLED)
    area_chat.see(tk.END)
    
    entrada_chat.delete(0, tk.END)
    threading.Thread(target=executar_processamento_em_segundo_plano, args=(msg, perfil, api_key), daemon=True).start()

def limpar_placeholder(event):
    if entrada_api_key.get() == "Insira sua Gemini API Key aqui (Opcional)":
        entrada_api_key.delete(0, tk.END)
        entrada_api_key.config(foreground="#000000")

janela = tk.Tk()
janela.title("EcoCognição - Sistema Híbrido Cognitivo")
janela.geometry("1100x650")
janela.configure(bg="#f4f6f9")

# --- PAINEL DA ESQUERDA ---
frame_perfil = tk.LabelFrame(janela, text=" Configurações do Sistema ", font=("Arial", 10, "bold"), padx=15, pady=15, bg="#ffffff", fg="#1a73e8")
frame_perfil.pack(side=tk.LEFT, fill=tk.Y, padx=15, pady=15)

tk.Label(frame_perfil, text="Data de Nascimento (DD/MM/AAAA):", bg="#ffffff", font=("Arial", 9, "bold")).pack(anchor=tk.W, pady=2)
entrada_nascimento = tk.Entry(frame_perfil, font=("Arial", 10), width=28)
entrada_nascimento.insert(0, "19/05/1978")
entrada_nascimento.pack(anchor=tk.W, pady=5)

tk.Label(frame_perfil, text="Identidade de Gênero:", bg="#ffffff", font=("Arial", 9, "bold")).pack(anchor=tk.W, pady=2)
combo_genero = ttk.Combobox(frame_perfil, values=["Masculino", "Feminino", "Não-Binário", "Outro"], width=26, state="readonly")
combo_genero.set("Masculino")
combo_genero.pack(anchor=tk.W, pady=5)

tk.Label(frame_perfil, text="Etnia / Raça / Identidade Social:", bg="#ffffff", font=("Arial", 9, "bold")).pack(anchor=tk.W, pady=2)
combo_etnia = ttk.Combobox(frame_perfil, values=["Parda", "Negra", "Branca", "Indígena", "Amarela"], width=26, state="readonly")
combo_etnia.set("Parda")
combo_etnia.pack(anchor=tk.W, pady=5)

tk.Frame(frame_perfil, height=2, bd=1, relief=tk.SUNKEN, bg="#e0e0e0").pack(fill=tk.X, pady=15)

tk.Label(frame_perfil, text="Chave de API Gemini (Conexão Real):", bg="#ffffff", font=("Arial", 9, "bold")).pack(anchor=tk.W, pady=2)
entrada_api_key = tk.Entry(frame_perfil, font=("Arial", 9), width=28, fg="#999999")
entrada_api_key.insert(0, "Insira sua Gemini API Key aqui (Opcional)")
entrada_api_key.bind("<FocusIn>", limpar_placeholder)
entrada_api_key.pack(anchor=tk.W, pady=5)

# --- PAINEL DA DIREITA ---
frame_chat = tk.Frame(janela, bg="#f4f6f9")
frame_chat.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=15, pady=15)

area_chat = tk.Text(frame_chat, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 10), bg="#ffffff", bd=0, padx=10, pady=10)
area_chat.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

area_chat.tag_config("usuario", foreground="#1a73e8", font=("Arial", 10, "bold"))
area_chat.tag_config("ia", foreground="#202124")

frame_entrada = tk.Frame(frame_chat, bg="#f4f6f9")
frame_entrada.pack(fill=tk.X)

entrada_chat = tk.Entry(frame_entrada, font=("Arial", 11), bd=1, relief=tk.SOLID)
entrada_chat.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6, padx=(0, 10))
entrada_chat.bind("<Return>", lambda event: iniciar_envio())

botao_enviar = tk.Button(frame_entrada, text="Enviar", command=iniciar_envio, bg="#1a73e8", fg="#ffffff", font=("Arial", 10, "bold"), width=12, bd=0, cursor="hand2")
botao_enviar.pack(side=tk.RIGHT, ipady=6)

area_chat.config(state=tk.NORMAL)
area_chat.insert(tk.END, "🤖 IA: Olá! Como se sente em relação aos seus desafios de hoje?\n")
area_chat.insert(tk.END, f"{'='*75}\n\n")
area_chat.config(state=tk.DISABLED)

janela.mainloop()