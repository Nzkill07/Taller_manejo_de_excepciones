class Consola:
    def __init__(self, juego):
        self.juego = juego

    def iniciar_juego(self):
        for frame in range(10):
            print("Frame", frame + 1)
            while True:
                try:
                    roll1 = input("Puntaje del primer lanzamiento ('X' para strike): ")
                    roll1 = roll1.upper()
                    if roll1 == 'X':
                        self.juego.roll(10)
                    else:
                        roll1 = int(roll1)
                        if roll1 < 0 or roll1 > 10:
                            raise ValueError("El puntaje debe estar entre 0 y 10")
                        self.juego.roll(roll1)
                    break
                except ValueError as e:
                    print(e)

            if roll1 != 'X' and int(roll1) < 10:
                while True:
                    try:
                        roll2 = input("Puntaje del segundo lanzamiento ('/' para spare): ")
                        if roll2 == '/':
                            self.juego.roll(10 - roll1)
                        else:
                            roll2 = int(roll2)
                            if roll2 < 0 or roll2 > 10 - roll1:
                                raise ValueError("El puntaje debe estar entre 0 y {}".format(10 - roll1))
                            self.juego.roll(roll2)
                        break
                    except ValueError as e:
                        print(e)

            print("Puntaje total hasta ahora:", self.juego.score())

        if self.juego.frames[-1].is_strike() or self.juego.frames[-1].is_spare():
            print("Frame 11")
            while True:
                try:
                    roll1_frame11 = input("Puntaje del primer lanzamiento: ")
                    roll1_frame11 = roll1_frame11.upper()
                    if roll1_frame11 == 'X':
                        self.juego.roll(10)
                    else:
                        roll1_frame11 = int(roll1_frame11)
                        if roll1_frame11 < 0 or roll1_frame11 > 10:
                            raise ValueError("El puntaje debe estar entre 0 y 10")
                        self.juego.roll(roll1_frame11)

                    if roll1_frame11 != 'X' and int(roll1_frame11) < 10:
                        while True:
                            try:
                                roll2_frame11 = input("Puntaje del segundo lanzamiento (si aplica): ")
                                if roll2_frame11 == '/':
                                    self.juego.roll(10 - int(roll1_frame11))
                                else:
                                    roll2_frame11 = int(roll2_frame11)
                                    if roll2_frame11 < 0 or roll2_frame11 > 10 - int(roll1_frame11):
                                        raise ValueError("El puntaje debe estar entre 0 y {}".format(10 - int(roll1_frame11)))
                                    self.juego.roll(roll2_frame11)
                                break
                            except ValueError as e:
                                print(e)
                    break
                except ValueError as e:
                    print(e)

        print("Puntaje total:", self.juego.score())
