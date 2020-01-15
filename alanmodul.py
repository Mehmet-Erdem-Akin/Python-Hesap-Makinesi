# -*- coding: utf-8 -*-

def dikdortgenA(uzunkenar,kisakenar):
    """
    (Dikdörtgenin Alanını Hesaplar)
    (Girilem uzun kenar ile kısa kenarı çarpar)
    """
    return uzunkenar * kisakenar
    
def kareA(kenar1):
    """
    (Karenin Alanını Hesaplar)
    (Girilen bir kenarı kendisi ile çarpar)
    """
    return kenar1 * kenar1

def ucgenA(taban,yukseklık):
    """
    (Üçgenin Alanını Hesaplar)
    (Girilen taban alanı ile yüksekliği çarpıp 2' ye böler)
    """
    return (taban * yukseklık) / 2 