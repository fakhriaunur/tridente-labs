# 🛡️ Tridente Labs: A DevSecOps Approach to Critical Infrastructure Security

## Ringkasan Proyek

Tridente Labs adalah sebuah *proof-of-concept* laboratorium keamanan siber yang dirancang untuk mensimulasikan dan memitigasi ancaman terhadap infrastruktur kritis, dengan studi kasus PT Pupuk Indonesia (PI). Proyek ini mengimplementasikan paradigma **"IT Tridente Practitioner"**, yang mengintegrasikan tiga pilar utama keamanan:

* **Architecture (CASP+):** Merancang sistem yang aman sejak awal (*secure by design*).
* **Offense (PenTest+):** Mensimulasikan serangan untuk memvalidasi pertahanan.
* **Defense (CySA+):** Memonitor dan merespons ancaman secara proaktif.

Lab pertama, **OT Security Simulator**, berfokus pada perlindungan sistem kontrol industri (ICS/OT) dari serangan siber seperti *ransomware*.

## Arsitektur Lab

Lab ini berjalan di dalam sebuah *cluster* Kubernetes (`kind`) tunggal yang mensimulasikan beberapa komponen jaringan terisolasi: