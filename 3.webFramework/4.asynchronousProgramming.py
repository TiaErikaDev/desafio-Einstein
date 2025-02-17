import asyncio
import time

#Funcao síncrona
def chamar_paciente_sincrono(nome, tempo):
    print(f"📢Chamando {nome}...")
    time.sleep(tempo)
    print(f"✅{nome} atendido!")
    
#Funcao assíncrona
async def chamar_paciente_assincrono(nome, tempo):
    print(f"📢Chamando {nome}...")
    await asyncio.sleep(tempo)
    print(f"✅{nome} atendido!")

#Funcao principal
async def main():
    pacientes = [("Ana", 2), ("Bruno", 1), ("Carlos", 3)]
    
    print("\n Triagem SINCRONA...\n")
    inicio = time.time()
    for nome, tempo in pacientes:
        chamar_paciente_sincrono(nome, tempo)
    print(f"\nTempo total: {time.time() - inicio:.1f} segundos\n")
    
    print("\n Triagem ASSINCRONA...\n")
    inicio = time.time()
    tarefas = [chamar_paciente_assincrono(nome, tempo) for nome, tempo in pacientes]
    await asyncio.gather(*tarefas)
    print(f"\nTempo total: {time.time() - inicio:.1f} segundos\n")
    
#Executar funcao principal
asyncio.run(main())
