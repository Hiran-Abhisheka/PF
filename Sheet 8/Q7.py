while True:
    avg=int(input("Ener average: "))
    def points(avg):
        if 90 <= avg <= 100:
            return 4
        elif 80 <= avg < 90:
            return 3
        elif 70 <= avg < 80:
            return 2
        elif 60 <= avg < 70:
            return 1
        else:
            return 0
    def main():
        qpoints=points(avg)
        print(f"The qulity points for an average  of {avg} is: {qpoints}")
        points(avg)
    if __name__=='__main__':
        main()