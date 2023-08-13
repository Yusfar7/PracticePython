import time 
start_time = time.time() # Geçerli zaman damgasını al # Uzun süren bir işlem simülasyonu
time.sleep( 2 ) 
end_time = time.time() # İşlemin bitiş zaman damgasını al 
elapsed_time = end_time - start_time
print(f"Geçen süre: {elapsed_time:.2f} saniye")