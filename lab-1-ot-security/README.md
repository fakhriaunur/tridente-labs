Dokumen ini adalah cetak biru operasional akhir untuk Lab 1: OT Security Simulator, sebuah proyek yang dirancang untuk mendemonstrasikan kapabilitas IT Tridente Practitioner.

Struktur Proyek Final (Pohon Direktori GitHub)
tridente-labs/
│
├── .gitignore
├── README.md             # Halaman utama & pitch deck proyek
│
└── lab-1-ot-security/
    │
    ├── kind-config.yaml      # Konfigurasi cluster (PLC, HMI)
    ├── openplc-deployment.yaml # Denah deployment OpenPLC (Target)
    ├── scadabr-deployment.yaml # Denah deployment ScadaBR (HMI)
    ├── wazuh-deployment.yaml   # Denah deployment Wazuh Manager (SIEM)
    ├── wazuh-dashboard-deployment.yaml   # Denah deployment Wazuh Dashboard	
    ├── zeek-deployment.yaml    # Denah deployment Zeek (Official Image)
    │
    ├── attacker/
    │   └── plc_attacker.py     # Script serangan Modbus (Pilar Offense)
    │
    ├── plc-logic/
    │   └── motor_logic.st      # Logika program PLC (Start/Stop Motor)
    │
    └── defense/
        └── detection_rules.xml   # Aturan deteksi custom Wazuh (Pilar Defense)

Fase Operasi
Fase 0: Intelijen & Strategi
Tujuan: Membangun fondasi strategis sebelum aspek teknis.

Aksi Kunci: Analisis OSINT terhadap PI, branding persona "The Ghost", konseptualisasi kerangka kerja "IT Tridente" & "Legal-IT Nexus".

Fase 1: Pembangunan Infrastruktur Kritis
Tujuan: Mendirikan lingkungan lab OT yang fungsional di satu mesin.

Artefak & SOP Kunci:

Teknologi: Podman Desktop, kind, kubectl.

Deployment PLC & HMI: Menggunakan image Docker publik teruji (fdamador/openplc, bitelxux/scadabr).

Logika PLC: Meng-upload motor_logic.st ke OpenPLC untuk mensimulasikan proses industri.

Fase 2: Eksekusi Serangan Terkontrol
Tujuan: Mensimulasikan sabotase realistis terhadap proses industri.

Artefak Kunci:

plc_attacker.py: Dijalankan dari host machine untuk menyerang port Modbus PLC.

Fase 3: Pembangunan Pertahanan Berlapis
Tujuan: Mendirikan arsitektur pertahanan yang komprehensif.

Artefak Kunci:

Dasar Pertahanan (SIEM): Mendeploy Wazuh Manager (wazuh-deployment.yaml) sebagai "otak" SIEM di pod terisolasi.

Pertahanan Jaringan (NSM): Mendeploy Zeek (zeek-deployment.yaml) menggunakan image resmi zeek/zeek:lts sebagai DaemonSet untuk memonitor seluruh lalu lintas jaringan.

Desain Aturan Deteksi (detection_rules.xml): Merancang aturan berlapis di Wazuh (Otorisasi, Volumetrik, Kontekstual) yang siap untuk mengkorelasikan log dari Zeek dan agen HIDS.

Fase 4: Visualisasi & Pelaporan (Stretch Goal)
Tujuan: Memberikan antarmuka visual untuk hasil analisis SIEM.

Aksi Kunci: Mendeploy Wazuh Dashboard di pod terpisah dan mengekspos port-nya ke host machine untuk keperluan presentasi dan verifikasi alert.