<!DOCTYPE html>
<html>

<body>
  <h1>Samba Dosya Paylaşımı Scripti</h1>
  <p>Bu Python scripti, Ubuntu Server üzerinde otomatik olarak SMB dosya paylaşım hizmeti oluşturmanızı sağlar.</p>

  <h2>Kurulum</h2>
  <ol>
    <li>Ubuntu Server üzerinde root yetkilerine sahip bir kullanıcıyla oturum açın.</li>
    <li>Gerekli bağımlılıkları yüklemek ve Samba paketini indirmek için aşağıdaki komutları çalıştırın:</li>
  </ol>
  <pre>
    <code>
      $ <span class="command">sudo apt update</span>
      $ <span class="command">sudo apt install samba</span>
    </code>
  </pre>
  
  <h2>Kullanım</h2>
  <ol>
    <li>Script dosyasını indirin ve çalıştırılabilir yapmak için aşağıdaki komutları çalıştırın:</li>
  </ol>
  <pre>
    <code>
      $ <span class="command">wget https://example.com/samba_script.py</span>
      $ <span class="command">chmod +x samba_script.py</span>
    </code>
  </pre>
  <ol start="2">
    <li>Scripti düzenleyerek paylaşım adını ve paylaşılacak dizinin yolunu belirleyin:</li>
  </ol>
  <pre>
    <code>
      $ <span class="command">nano samba_script.py</span>
      <span class="comment"># Paylaşım adı ve dizinini belirleyin</span>
      share_name = 'MyShare'
      share_path = '/path/to/shared/folder'
    </code>
  </pre>
  <ol start="3">
    <li>Scripti çalıştırın:</li>
  </ol>
  <pre>
    <code>
      $ <span class="command">sudo ./samba_script.py</span>
    </code>
  </pre>
  <p>Samba dosya paylaşım hizmeti oluşturulacak ve belirttiğiniz paylaşım adı ve dizini kullanarak dosyalarınızı paylaşabileceksiniz.</p>
  
  <h2>Lisans</h2>
  <p>Bu script MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için <a href="https://example.com/LICENSE">LİSANS</a> dosyasını inceleyebilirsiniz.</p>
</body>
</html>
