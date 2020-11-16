detik = int(input("Ketik nilai detik ="))
D = detik
H = D / 86400
D = D % 86400
J = D/3600
D = D % 3600
M = D/60
D = D % 60
print(detik, "detik = ", H, " hari + ", J,
      " jam + ", M, " menit + ", D, " detik")
