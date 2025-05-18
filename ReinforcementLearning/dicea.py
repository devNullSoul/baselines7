import numpy as np
from numpy.random import default_rng
rng = default_rng(seed=100)

def experiment_one():
    state_space = [1,0]
    action_space = [1,0]

    def epoch():
        # Es wird ein Münzwurf simuliert. Es handelt sich um eine
        # Laplace-Verteilung mit Erwartungswert 0.5.
        # Das bedeutet, beide Seiten der Münze sind gleich wahrscheinlich.
        #
        # epoc() startet ein Experiment mit 100 Wetten. Die Variable bet
        # definiert ob wie auf Kopf oder Zahl setzen (1 oder 0). Die Variable
        # coin_toss definiert ob der Wurf Kopf oder Zahl (1 oder 0) war.
        # Liegen wir mit unserer Wette richtig (bet == coin_toss), dann erhalten
        # wir 1 CHF und addieren es zu unserem Reward.
        #
        # Da es win Laplace-Experiment ist mit Erwartungswert 0.5, erwarten wir
        # eine Reward von ca. 50 CHF bei 100 Versuchen
        #
        reward = 0
        for _ in range(100): # Ein Experiment besteht aus 100 Münzwurfen.
            bet = rng.choice(action_space) # Unsere Wette
            coin_toss = rng.choice(state_space) # Der Münzwurf, Kopf oder Zahl
            if bet == coin_toss:
                reward += 1 # Wenn wir richtig liegen, gewinnen wir 1 CHF
        return reward

    # Wir führen das Zufallsexperiment mit je 100 Münzwurfen 250 Mal aus.
    # 
    rl = np.array([epoch() for _ in range(250)])
    print(f"rl = {rl}")
    print(f"rl.mean() = {rl.mean()}")

experiment_one()
