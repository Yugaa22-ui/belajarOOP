from data.nasabah_data import nasabah_list

class BankService:
    @staticmethod
    def setor_dana(no_rek: str, jumlah: int):
        if no_rek in nasabah_list:
            nasabah_list[no_rek]["saldo"] += jumlah
            return nasabah_list[no_rek]
        else:
            raise ValueError("Nomor rekening tidak ditemukan.")

    @staticmethod
    def tarik_dana(no_rek: str, jumlah: int):
        if no_rek in nasabah_list:
            saldo_akhir = nasabah_list[no_rek]["saldo"] - jumlah
            if saldo_akhir < 35000:
                raise ValueError("Saldo tidak mencukupi untuk penarikan.")
            nasabah_list[no_rek]["saldo"] = saldo_akhir
            return nasabah_list[no_rek]
        else:
            raise ValueError("Nomor rekening tidak ditemukan.")
