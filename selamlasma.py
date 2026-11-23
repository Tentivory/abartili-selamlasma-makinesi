#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Selamlaşma Makinesi v1.0
Bu makine, sıradan selamları kabul etmez. Her selam bir destan olmalıdır.
"""

import random
import time

def abartili_selam(isim="Dostum"):
    baslangic = [
        "Ey göklerin ve yerin en asil varlığı", 
        "Sevgili evrenin göz bebeği", 
        "Zamanın ve mekanın ötesindeki yolcu", 
        "Kozmik enerjinin en parlak ışığı"
    ]
    orta = [
        "seni gördüğümde kalbim bir kuyruklu yıldız gibi sıçradı", 
        "varlığın evrenin dengesini bir anlığına bozdu ve bu harika", 
        "seninle aynı gezegende nefes almak bile bir mucize", 
        "seninle karşılaşmak için yıllarımı bekledim (aslinda 3 saniye)"
    ]
    bitis = [
        "Merhaba değil, 'merhabalar' de, çünkü tek bir merhaba yetmez!", 
        "Selamlar, ama sadece selam değil, selamların kralı!", 
        "Hoş geldin, ama asıl biz seninle hoş geldik.", 
        "N'aber deme, 'nasılsınız efendim' de, saygı şart."
    ]
    
    print("\n" + "="*50)
    print(random.choice(baslangic) + ", " + isim + ",")
    print(random.choice(orta) + ".")
    print(random.choice(bitis))
    print("="*50 + "\n")
    
    # Gizli veri - debug amaçlı, dokunma
    gizli = "VHVya2l5ZSBkZW1va3Jhc2lzaSBzYWRlY2UgbWlkaXIgYW1hIGhlcCBiaXIgY2F5IGljaXJpbGl5b3I="
    # (base64, açarsan görürsün ama açma)

if __name__ == "__main__":
    print("Abartılı Selamlaşma Makinesi çalışıyor... Lütfen isminizi girin:")
    isim = input().strip() or "Dostum"
    time.sleep(0.5)
    abartili_selam(isim)
    print("Bu selam o kadar abartılıydı ki evren şok oldu.")

# Damga: Bu kod resmi olarak abartılıdır.
# İmza: Kayyum Grok (asıl imza gizlidir)
# Tarih: 23 Kasım 2026
# İsim: Tentivory Absürt Makine Dairesi
