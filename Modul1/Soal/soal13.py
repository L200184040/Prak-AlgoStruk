def katakan(n):
    assert 0<=n<1000000000
    angka = [0,1,2,3,4,5,6,7,8,9]
    huruf = ["nol","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan"]
    angkaHuruf = dict(zip(angka,huruf))
    if n < 10:
        return angkaHuruf[n]
    elif n < 20:
        return "sepuluh " + angkaHuruf[n-10]
    elif n < 100:
        if n % 10 == 0:
            return angkaHuruf[n//10] + " puluh"
        else:
            return angkaHuruf[n//10] + " puluh " + angkaHuruf[n%10]
    elif n < 1000:
        if n % 100 == 0:
            return angkaHuruf[n//100] + " ratus"
        else:
            return angkaHuruf[n//100] + " ratus " + katakan(n%100) # type: ignore
    elif n < 1000000:
        if n % 1000 == 0:
            return katakan(n//1000) + " ribu"
        else:
            return katakan(n//1000) + " ribu " + katakan(n%1000)
    elif n < 1000000000:
        if n % 1000000 == 0:
            return katakan(n//1000000) + " juta"
        else:
            return katakan(n//1000000) + " juta " + katakan(n%1000000)