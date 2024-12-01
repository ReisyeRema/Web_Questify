from datetime import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ContactForm, CreateUserForm,ProfileUpdateForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileUpdateForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Kelas
from .models import ModulPembelajaran,Transaksi
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import midtransclient

from django.http import JsonResponse
import midtransclient
from .models import Kelas, Transaksi
from django.contrib.auth.models import User
import uuid

#Create your views here.

def index(request):
    data = "Hello, Questify!"  # Variabel data untuk ditampilkan
    return render(request, 'questify_app/index.html', context={'data': data})
=======
from django.contrib.auth.models import User
from .models import ModulPembelajaran, Soal, JawabanUser, Nilai, UserProfile, Kelas, PercobaanTerakhir
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now, timedelta
from django.utils.dateparse import parse_datetime
from django.db.models import Sum
>>>>>>> 30bc9755eb7ab9f5ee8e23df1d22584c7f570c1e


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Simpan data dari form ke database
            form.save()

            # Mengirimkan email setelah formulir berhasil dikirim
            send_mail(
                'Pesan Kontak Baru',  # Subjek email
                f'Nama: {form.cleaned_data["name"]}\n'
                f'Telepon: {form.cleaned_data["phone"]}\n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Komentar: {form.cleaned_data["comment"]}',  # Isi email
                settings.EMAIL_HOST_USER,  # Pengirim
                [settings.EMAIL_HOST_USER],  # Penerima
                fail_silently=False,
            )

            # Menampilkan pesan sukses
            messages.success(request, "Pesan Anda telah berhasil dikirim!")
            return redirect('index')  # redirect untuk mengosongkan form
    else:
        form = ContactForm()

    # Ambil semua data kelas dari database
    kelas_list = Kelas.objects.all()

    return render(request, 'questify_app/pages/index.html', {
        'form': form,
        'kelas_list': kelas_list,  # Kirim data kelas ke template
    })

<<<<<<< HEAD
=======

>>>>>>> 30bc9755eb7ab9f5ee8e23df1d22584c7f570c1e

def register(request):
    form = CreateUserForm()


    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for {username}.  Please login')

            return redirect('questify_app:login')

    context = {'form':form}
    return render(request, 'questify_app/pages/register.html', context)



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect berdasarkan peran pengguna
            if user.is_staff or user.is_superuser:  # Admin atau staff
                return redirect(reverse('admin:index'))  # Halaman admin bawaan Django
            else:  # User biasa
                return redirect('questify_app:home')  # Halaman user biasa
        else:
            messages.error(request, 'Username atau password salah')

    return render(request, 'questify_app/pages/login.html')

@login_required
def home(request):
    return render(request, 'questify_app/pages/home.html')



@login_required(login_url='/questify_app/login/')
def userprofile(request):
    user = request.user

    # Periksa apakah pengguna sudah memiliki profil
    if not hasattr(user, 'profile'):
        UserProfile.objects.create(user=user)  # Jika tidak ada, buatkan profil baru

    # Jika metode POST, proses perubahan profil
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil Anda telah diperbarui!')
            return redirect('questify_app:userprofile')  # Redirect ke halaman profil setelah perubahan
    else:
        # Jika GET, tampilkan profil pengguna yang sedang login
        form = ProfileUpdateForm(instance=user)

    return render(request, 'questify_app/pages/userprofile.html', {'form': form, 'user': user})


@login_required(login_url='/questify_app/login/')
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('questify_app:userprofile')  # Ganti 'profile' dengan nama rute Anda
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'questify_app/pages/userprofile.html', {'form': form})




@login_required(login_url='/questify_app/login/')
def semuakelas(request):
    kelas_list = Kelas.objects.all()
    return render(request, 'questify_app/pages/semuakelas.html', {'kelas_list': kelas_list})
from django.http import JsonResponse
import midtransclient
from .models import Kelas, Transaksi
from django.contrib.auth.models import User

def payment(request):
    if request.method == 'POST':
        # Parse JSON data dari permintaan POST
        kelas_id = request.POST.get('kelas_id')
        amount = request.POST.get('amount')
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        
        print(user_id, amount)
        
        snap = midtransclient.Snap(
            is_production=False,
            server_key='SB-Mid-server-IxGL8J0daVsu14JPWym77KPT'
        )
        
        # Build API parameter
        param = {
            "transaction_details": {
                "order_id": str(uuid.uuid4()),  # Sesuaikan order_id jika diperlukan
                "gross_amount": amount
            },
            "credit_card": {
                "secure": True
            },
            "customer_details": {
                "first_name": first_name,
                # "last_name": "pratama",
                # "email": "budi.pra@example.com",
                # "phone": "08111222333"
            }
        }

        # Buat transaksi di Midtrans dan dapatkan token
        transaction = snap.create_transaction(param)
        transaction_token = transaction['token']
        
        # Simpan data transaksi ke database
        kelas = Kelas.objects.get(id=kelas_id)
        user = User.objects.get(id=user_id)
        Transaksi.objects.create(
            user=user,
            kelas=kelas,
            amount=amount,
            link_payment="https://app.sandbox.midtrans.com/snap/v2/vtweb/" + transaction_token
        )
        
        # Mengembalikan token transaksi sebagai JSON
        return JsonResponse({"token": transaction_token})

    return JsonResponse({"error": "Invalid request"}, status=400)




@login_required(login_url='/questify_app/login/')
def pilihkelas(request, kelas_id):
    # Mendapatkan objek Kelas berdasarkan ID
    kelas = get_object_or_404(Kelas, id=kelas_id)
    
    # Memfilter modul berdasarkan kelas yang dipilih
    modul_list = ModulPembelajaran.objects.filter(kelas=kelas)
    
    context = {
        'kelas': kelas,
        'modul_list': modul_list,
    }
    
    return render(request, 'questify_app/pages/pilihkelas.html', context)




@login_required(login_url='/questify_app/login/')
def detailkelas(request, id):
    modul = get_object_or_404(ModulPembelajaran, id=id)
    kelas = modul.kelas  # Ambil kelas yang terkait dengan modul
    context = {
        'modul': modul,
        'kelas': kelas  # Kirimkan objek kelas ke template
    }
    return render(request, 'questify_app/pages/detailkelas.html', context)




@login_required(login_url='/questify_app/login/')
def hasilnilai(request):
    user = request.user
    hasil_data = (
        Nilai.objects.filter(user=user)
        .select_related('modul', 'modul__kelas')
        .order_by('-tanggal_percobaan', '-percobaan_ke', '-id')  # Urutkan berdasarkan tanggal, percobaan_ke, dan id
    )

    # Menambahkan informasi benar, salah, total soal untuk setiap nilai
    for result in hasil_data:
        # Filter JawabanUser berdasarkan percobaan_ke dan modul untuk menghitung benar dan salah
        total_benar = JawabanUser.objects.filter(user=user, percobaan_ke=result.percobaan_ke, soal__modul=result.modul, status=True).count()
        total_salah = JawabanUser.objects.filter(user=user, percobaan_ke=result.percobaan_ke, soal__modul=result.modul, status=False).count()

        # Menyimpan hasil ke dalam result untuk ditampilkan di template
        result.benar = total_benar
        result.salah = total_salah
        result.total_soal = result.modul.soal.count()  # Total soal dalam modul
        result.tanggal = result.tanggal_percobaan  # Tanggal percobaan

    return render(request, 'questify_app/pages/hasilnilai.html', {'hasil_data': hasil_data})


@login_required(login_url='/questify_app/login/')
def halamanselesai(request, modul_id, nilai_total):
    modul = get_object_or_404(ModulPembelajaran, id=modul_id)
    # Ambil percobaan terakhir yang dilakukan oleh pengguna untuk modul ini dari database
    percobaan_terakhir = PercobaanTerakhir.objects.filter(user=request.user, modul=modul).first()
    if percobaan_terakhir:
        percobaan_ke = percobaan_terakhir.percobaan_ke
    else:
        percobaan_ke = 1  # Jika tidak ada data percobaan sebelumnya, mulai dari percobaan pertama

    kelas = modul.kelas  # Ambil kelas yang terkait dengan modul


    jawaban_user = JawabanUser.objects.filter(
        user=request.user,
        soal__modul=modul,
        percobaan_ke=percobaan_ke
    )

    return render(request, 'questify_app/pages/halamanselesai.html', {
        'modul': modul,
        'nilai_total': nilai_total,
        'percobaan_ke': percobaan_ke,
        'jawaban_user': jawaban_user,
        'kelas': kelas,
    })



@login_required(login_url='/questify_app/login/')
def langganan(request):
    kelas_list = Kelas.objects.all()
    return render(request, 'questify_app/pages/langganan.html', {'kelas_list': kelas_list})



@login_required(login_url='/questify_app/login/')
def review(request, percobaan_ke, modul_id):
    user = request.user

    # Ambil data soal dan jawaban user berdasarkan percobaan dan modul
    jawaban_list = JawabanUser.objects.filter(
        user=user,
        soal__modul_id=modul_id,
        percobaan_ke=percobaan_ke
    )
    
    # Ambil objek modul berdasarkan ID modul
    modul = get_object_or_404(ModulPembelajaran, id=modul_id)

    # Hitung jumlah soal yang dijawab benar dan salah
    benar = jawaban_list.filter(status=True).count()
    salah = jawaban_list.filter(status=False).count()

    # Hitung durasi pengerjaan
    if jawaban_list.exists():
        waktu_mulai = jawaban_list.first().waktu_jawab
        waktu_selesai = jawaban_list.last().waktu_jawab
        durasi = waktu_selesai - waktu_mulai
    else:
        durasi = timezone.timedelta()

    # Format durasi menjadi HH:MM:SS tanpa desimal
    durasi_str = str(durasi).split('.')[0]

    # Hitung nilai akhir berdasarkan jumlah soal yang benar
    total_soal = jawaban_list.count()
    nilai = (benar / total_soal) * 100 if total_soal > 0 else 0  # Menghitung persentase benar

    # Ubah nilai menjadi integer untuk menghilangkan koma
    nilai = int(nilai)  # Mengkonversi nilai ke bilangan bulat tanpa koma

    # Ambil data nilai untuk percobaan ini (jika ada)
    nilai_data = Nilai.objects.filter(
        user=user,
        modul=modul,
        percobaan_ke=percobaan_ke
    ).first()

    # Jika data nilai belum ada, buat baru
    if not nilai_data:
        Nilai.objects.create(
            user=user,
            modul=modul,
            jumlah_nilai=nilai,
            waktu_pengajaran=durasi,
            percobaan_ke=percobaan_ke
        )

    context = {
        'jawaban_list': jawaban_list,
        'nilai': nilai,
        'total_soal': total_soal,
        'benar': benar,
        'salah': salah,
        'durasi': durasi_str,  # Menggunakan durasi yang sudah diformat
        'modul': modul,
        'percobaan_ke': percobaan_ke,
    }

    return render(request, 'questify_app/pages/review.html', context)


@login_required(login_url='/questify_app/login/')
def metodepembayaran(request):
    return render(request, 'questify_app/pages/metodepembayaran.html')

@login_required(login_url='/questify_app/login/')
def cekbeli(request):
    return render(request, 'questify_app/pages/cekbeli.html')

<<<<<<< HEAD
# @login_required(login_url='/accounts/login/')
# def payment(request):
#     return render(request, 'questify_app/pages/payment.html')
=======
@login_required(login_url='/questify_app/login/')
def payment(request):
    return render(request, 'questify_app/pages/payment.html')
>>>>>>> 30bc9755eb7ab9f5ee8e23df1d22584c7f570c1e

@login_required(login_url='/questify_app/login/')
def daftartransaksi(request):
    return render(request, 'questify_app/pages/daftar_transaksi.html')

@login_required(login_url='/questify_app/login/')
def detailtransaksi(request):
    return render(request, 'questify_app/pages/detailtransaksi.html')

<<<<<<< HEAD
#keperluang midtrans
# @login_required
# def initiate_payment(request):
#     # Ambil metode pembayaran dari parameter URL
#     bank = request.GET.get('bank')
    
#     if not bank:
#         return HttpResponse("Metode pembayaran tidak ditemukan", status=400)
    
#     # Logika untuk memulai proses pembayaran menggunakan Midtrans
#     # Misalnya, mengatur parameter dan mengirim permintaan ke Midtrans
    
#     # Redirect atau tampilkan halaman sesuai kebutuhan setelah proses pembayaran
#     return HttpResponse(f"Proses pembayaran menggunakan bank {bank} dimulai.", status=200)
=======
@login_required(login_url='/questify_app/login/')
def soal(request, modul_id, soal_id=None):
    modul = get_object_or_404(ModulPembelajaran, id=modul_id)
    soal_list = Soal.objects.filter(modul=modul).order_by('id')

    # Cek percobaan terakhir di database untuk pengguna dan modul
    percobaan_terakhir = PercobaanTerakhir.objects.filter(user=request.user, modul=modul).first()
    if percobaan_terakhir:
        percobaan_ke = percobaan_terakhir.percobaan_ke
    else:
        percobaan_ke = 1  # Mulai dari percobaan pertama jika belum ada

    if soal_id is None:
        soal = soal_list.first()
        nomor_soal = 1
    else:
        soal = get_object_or_404(soal_list, id=soal_id)
        nomor_soal = list(soal_list).index(soal) + 1

    next_soal = soal_list.filter(id__gt=soal.id).first()
    is_last_question = next_soal is None

    pilihan_user = None
    if request.method == 'POST':
        pilihan_user = request.POST.get(f'pilihan_user_{soal.id}')
        if pilihan_user:
            status = pilihan_user == soal.jawaban
            JawabanUser.objects.create(
                user=request.user,
                soal=soal,
                pilihan_user=pilihan_user,
                status=status,
                percobaan_ke=percobaan_ke
            )

        if 'selesai' in request.POST:
            # Hitung nilai berdasarkan soal yang benar
            nilai_total = JawabanUser.objects.filter(
                user=request.user,
                soal__modul=modul,
                percobaan_ke=percobaan_ke,
                status=True
            ).aggregate(total_nilai=Sum('soal__nilai_jawaban'))['total_nilai'] or 0

            waktu_pengajaran = timedelta(seconds=request.session.get(f'modul_{modul_id}_time_spent', 0))
            # Cek apakah nilai sudah ada untuk percobaan ini
            nilai_data = Nilai.objects.filter(user=request.user, modul=modul, percobaan_ke=percobaan_ke).first()
            if not nilai_data:
                Nilai.objects.create(
                    user=request.user,
                    modul=modul,
                    jumlah_nilai=nilai_total,
                    waktu_pengajaran=waktu_pengajaran,
                    tanggal_percobaan=now(),
                    percobaan_ke=percobaan_ke
                )

            # Update percobaan ke untuk percakapan berikutnya
            percobaan_ke += 1
            PercobaanTerakhir.objects.update_or_create(
                user=request.user,
                modul=modul,
                defaults={'percobaan_ke': percobaan_ke}
            )

            return redirect('questify_app:halamanselesai', modul_id=modul.id, nilai_total=nilai_total)

        if next_soal:
            return redirect('questify_app:soal_detail', modul_id=modul.id, soal_id=next_soal.id)

    # Atur waktu pengerjaan
    session_key = f'modul_{modul_id}_time'
    start_time_str = request.session.get(f'{session_key}_start')
    end_time_str = request.session.get(f'{session_key}_end')

    if not start_time_str or not end_time_str:
        start_time = now()
        end_time = start_time + timedelta(minutes=modul.waktu_pengajaran)
        request.session[f'{session_key}_start'] = start_time.isoformat()
        request.session[f'{session_key}_end'] = end_time.isoformat()
    else:
        start_time = parse_datetime(start_time_str)
        end_time = parse_datetime(end_time_str)

    remaining_time = max(0, (end_time - now()).total_seconds())
    time_spent = max(0, (now() - start_time).total_seconds())
    request.session[f'modul_{modul_id}_time_spent'] = time_spent

    if remaining_time <= 0:
        # Waktu habis, kirim jawaban dengan nilai 0
        JawabanUser.objects.filter(user=request.user, percobaan_ke=percobaan_ke).delete()  # Hapus jawaban yang tidak terjawab
        return redirect('questify_app:pilihkelas', kelas_id=modul.kelas.id)  # Arahkan ke halaman pilih kelas


    pilihan = [
        ('A', soal.pilihan_a),
        ('B', soal.pilihan_b),
        ('C', soal.pilihan_c),
        ('D', soal.pilihan_d),
    ]

    return render(request, 'questify_app/pages/soal.html', {
        'soal': soal,
        'next_soal': next_soal,
        'nomor_soal': nomor_soal,
        'remaining_time': remaining_time,
        'is_last_question': is_last_question,
        'pilihan': pilihan,
        'pilihan_user': pilihan_user,
        'percobaan_ke': percobaan_ke,
        'modul': modul,
    })
>>>>>>> 30bc9755eb7ab9f5ee8e23df1d22584c7f570c1e
