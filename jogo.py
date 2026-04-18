import random

OPCOES = ["pedra", "papel", "tesoura"]

VENCE = {
    "pedra":   "tesoura",
    "papel":   "pedra",
    "tesoura": "papel",
}

def resultado(jogador, maquina):
    if jogador == maquina:
        return "Empate"
    if VENCE[jogador] == maquina:
        return "Você ganhou"
    return "Você perdeu"

def main():
    print("=== Pedra, Papel e Tesoura ===")
    placar = {"vitórias": 0, "derrotas": 0, "empates": 0}

    while True:
        print("\n[p] Pedra  [pa] Papel  [t] Tesoura  [0] Sair")
        entrada = input("Sua jogada: ").strip().lower()

        mapa = {"p": "pedra", "pa": "papel", "t": "tesoura"}

        if entrada == "0":
            break

        if entrada not in mapa:
            print("Jogada inválida.")
            continue

        jogador = mapa[entrada]
        maquina = random.choice(OPCOES)
        res = resultado(jogador, maquina)

        print(f"\nVocê: {jogador} | Máquina: {maquina}")
        print(f">>> {res}")

        if res == "Você ganhou":  placar["vitórias"] += 1
        elif res == "Você perdeu": placar["derrotas"]  += 1
        else:                      placar["empates"]   += 1

    print(f"\nPlacar final — V: {placar['vitórias']} | D: {placar['derrotas']} | E: {placar['empates']}")

if __name__ == "__main__":
    main()
