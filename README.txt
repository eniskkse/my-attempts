==>First run the TCPServer and then switch to operations in TCPClient.
==>ilk önce TCPServerı çalıştırıp sonrasında TCPClientte işlemlere geçiniz.

==> TCPServer'ı ikinci kez çalıştırırsanız satır 19 ve 20'yi yorum satırına çevirmeli veya silmelisiniz aksi takdirde 
database'i ve Tabloyu ikinci kez create'lemeye çalışacaktır ve hata verecektir.
==>If you run TCPServer a second time, you should comment lines 19 and 20 or delete it otherwise
It will try to create database and table a second time and will give an error.  

==>TCPServer ve TCPClient aynı dizinde olmalıdır.
==>TCPServer and TCPClient must be in the same directory.