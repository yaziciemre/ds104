import sys
import random
import time

harfler = "AaBbCcÇçDdEeƏəFfGgĞğHhXxIıİiJjKkQqLlMmNnOoÖöPpRrSsŞşTtUuÜüVvYyZz"
harfler = list(harfler)
harfler2 = harfler[:]

def randomIndex():
	return int(random.random() * (len( harfler2 ) - 1))

sifreleme = {}

for h in harfler:
	rasgele_secilen_karakter = harfler2[ randomIndex() ]
	sifreleme[h] = rasgele_secilen_karakter
	harfler2.remove( rasgele_secilen_karakter )

	print(h, "===", rasgele_secilen_karakter, harfler2)





# Alterntaif
harfler = "AaBbCcÇçDdEeƏəFfGgĞğHhXxIıİiJjKkQqLlMmNnOoÖöPpRrSsŞşTtUuÜüVvYyZz"
harfler = list(harfler)
harfler2 = harfler[:]
random.shuffle(harfler2)


print(harfler)
print(harfler2)


sifreleme2 = dict( zip( harfler, harfler2 ) )
print(sifreleme2)




def encypt( text: str ) -> str:


	sifrelenmis_metin = ""

	for i in range(len(text)): # 0, 1, 2, 3
		character = text[i] # t, e, s, t

		if character in sifreleme2:
			character = sifreleme2[ character ]
		

		sifrelenmis_metin = sifrelenmis_metin + character
		print(">>", text[i], character, sifrelenmis_metin)


	return sifrelenmis_metin


genel = """
Azərbaycan xarici işlər naziri Ceyhun Bayramov Qazaxıstana işgüzar səfərə yola düşüb.

Bu barədə Azərbaycan Xarici İşlər Nazirliyi məlumat yayıb.

Səfər çərçivəsində Almatı şəhərində Azərbaycan və Ermənistan xarici işlər nazirlərinin iki ölkə arasında “Sülhün və dövlətlərarası münasibətlərin təsis edilməsi haqqında ikitərəfli Saziş” layihəsi üzrə danışıqlarının növbəti raundunun, habelə Qazaxıstan baş nazirinin müavini, xarici işlər naziri ilə görüşlərin keçirilməsi nəzərdə tutulub.

Ulu öndər Heydər Əliyevin anadan olmasının 101-ci ildönümündə dövlət qurumlarının rəsmiləri onun xatirəsini məzarı başında anıblar. 

Oxu.Az xəbər verir ki, Prezident Administrasiyasının rəhbəri Samir Nuriyev, Azərbaycan Prezidentinin köməkçiləri Hikmət Hacıyev, Şahmar Mövsümov, Təhlükəsizlik Şurasının katibi Ramil Usubov, Təhlükəsizlik Şurasının katibinin müavini Mədət Quliyev, Milli Məclisin deputatları Fəxri xiyabanı ziyarət edənlər sırasındadırlar.

09:17

Ulu öndər Heydər Əliyev anadan olmasının 101-ci ildönümündə hörmətlə anılır.

Oxu.Az xəbər verir ki, dövlət qurumlarının nümayəndələri, rəsmilər onu Fəxri xiyabandakı məzarı başında anırlar. 

Baş nazir Əli Əsədov, birinci müavini Yaqub Eyyubov, müavinləri Şahin Mustafayev, Əli Əhmədov, müdafiə naziri Zakir Həsənov, Milli Məclisin sədri Sahibə Qafarova Fəxri xiyabanı ziyarət edənlər sırasındadırlar. 

 

08:55

Ulu öndər Heydər Əliyev anadan olmasının 101-ci ildönümündə hörmətlə anılır.

Oxu.Az xəbər verir ki, dövlət qurumlarının nümayəndələri, rəsmilər onun Fəxri xiyabandakı məzarını ziyarət edirlər.

Xatırladaq ki, bu gün Azərbaycanın eks-prezidenti, ümummilli lider Heydər Əliyevin anadan olmasından 101 il keçir.

Almaz Qasımova, Nəzrin Vahid



Mədəniyyət ictimaiyyəti Heydər Əliyev Fondunun 20 illiyi münasibətilə Mehriban Əliyevanı təbrik etdi
10 May, 2024
08:42
402
147
23

Ölkəmizin mədəniyyət ictimaiyyəti Heydər Əliyev Fondunun yaradılmasının 20 illik yubileyi münasibətilə Fondun rəhbəri, Azərbaycan Respublikasının Birinci vitse-prezidenti Mehriban Əliyevaya təbrik müraciəti ünvanlayıb.

Bu barədə Mədəniyyət Nazirliyindən bildirilib.

Təbrikdə qeyd olunur ki, müasir müstəqil Azərbaycanın qurucusu, xalqımızın ümummilli lideri Heydər Əliyevin xatirəsini əziz tutaraq, adının əbədiləşdirilməsi, onun dövlətçilik ideyalarının gələcək nəsillərə ötürülməsi, zəngin irsinin təbliğ edilməsi məqsədilə yaradılan Heydər Əliyev Fondu ölkəmizin milli-mənəvi və mədəni dəyərlərinin dünyada tanıdılması istiqamətində yorulmadan fəaliyyət göstərir: 

“Heydər Əliyev Fondu yarandığı gündən möhtərəm Prezident İlham Əliyevin həyata keçirdiyi uğurlu dövlət siyasətində yaxından iştirak edərək sizin rəhbərliyinizlə Azərbaycan mədəniyyətinin inkişafı, milli-mənəvi dəyərlərin, multikultural ənənələrin qorunması və onların həm ölkə daxilində, həm də beynəlxalq aləmdə təşviqində mühüm rol oynayır. Bu siyasətin ən mühüm istiqamətlərindən olan işğaldan azad edilmiş ərazilərdə bərpa-quruculuq işlərinin aparılmasında, müasir sosial-mədəni infrastrukturun qurulmasında, Azərbaycan mədəni irsinin ümumbəşəri dəyərlər qismində tanınmasında Fondun verdiyi töhfələr əvəzsizdir. Reallaşdırdığınız və dəstək olduğunuz yerli və beynəlxalq layihələr Azərbaycan mədəniyyətinin, tarixinin və dövlətçiliyinin bünövrələrini, xalqımızın özünə və ali dəyərlərə inamını möhkəmləndirir, mədəniyyətimizi hamı üçün əlçatan və doğma edir. Heydər Əliyev Fondunun Azərbaycanda və onun hüdudlarından kənarda müxtəlif maddi-mədəniyyət abidələrinin qorunması, bərpası və yenidən qurulması istiqamətində, eləcə də beynəlxalq mədəniyyət mübadiləsindəki misilsiz xidmətləri mədəniyyət ictimaiyyəti və xalqımız tərəfindən yüksək dəyərləndirilir”.


Azad edilmiş ərazilərdə 118,5 min hektar sahə mina və partlamamış hərbi sursatlardan təmizlənib
10 May, 2024
08:06
425
84
3

İşğaldan azad edilmiş ərazilərdə bu günədək 118 min 503 hektar sahə, o cümlədən yaşayış məntəqələri üzrə 18 min 143 hektar sahə mina və partlamamış hərbi sursatlardan təmizlənib.

Bu göstəricilər Azərbaycan Respublikası Prezidenti Administrasiyasının rəhbəri Samir Nuriyevin AZƏRTAC-dakı məqaləsində yer alıb.

Samir Nuriyev qeyd edib ki, bütün ölkədə olduğu kimi, işğaldan azad edilmiş ərazilərdə də Azərbaycan Respublikasının Birinci vitse-prezidenti Mehriban Əliyevanın rəhbərliyi ilə bu il fəaliyyətinin 20 ili tamam olan Heydər Əliyev Fondunun gördüyü işlər və həyata keçirdiyi layihələr xüsusi önəm daşıyır: 

“Əminliklə demək olar ki, Heydər Əliyev Fondunun elm, təhsil, mədəniyyət, səhiyyə, idman və ekoloji sahələrə aid proqram və layihələri, sosial problemlərin həllinə dəstəyi, xüsusi qayğıya ehtiyacı olan insanlara kömək göstərməsi, Azərbaycan həqiqətlərinin dünya ictimaiyyətinə çatdırılması, mədəniyyətimizin və milli-mənəvi dəyərlərimizin qorunub saxlanması və təbliği sahələrində həyata keçirdiyi layihələr ölkəmizin ictimaiyyəti tərəfindən böyük rəğbətlə qarşılanır”.


PA rəhbəri: “Laçın, Füzuli, Zəngilan, Ağdərəyə 1 727 keçmiş məcburi köçkün ailəsi qayıdıb”
10 May, 2024
07:58
1114
122
16

2022-ci il iyulun 19-dan bu günədək Laçın və Füzuli şəhərlərinə, Zəngilan rayonunun Ağalı, Ağdərə rayonunun Talış, Laçın rayonunun Zabux kəndlərinə ümumilikdə 1 727 keçmiş məcburi köçkün ailəsinin (6 754 nəfər) qayıdışı baş tutub.

Bu barədə Azərbaycan Respublikası Prezidenti Administrasiyasının rəhbəri Samir Nuriyev AZƏRTAC-dakı məqaləsində bildirib.

S.Nuriyev qeyd edib ki, işğaldan azad olunmuş ərazilərdə hazırda böyükmiqyaslı bərpa-quruculuq işləri həyata keçirilir, insanlar doğma yurd-yuvalarına dönürlər: 

“Azərbaycan dövlətinin heç bir kənar yardım olmadan, öz gücünə gördüyü işlərin miqyası həqiqətən də heyrət doğurmaya bilməz. Azərbaycan Prezidenti İlham Əliyev işğaldan azad olunmuş ərazilərin bərpası və yenidən qurulmasına şəxsən nəzarət edir, dövlətimizin başçısının tapşırıqları və dəyərli tövsiyələri işlərin tam və məsuliyyətlə icrasına etibarlı zəmin yaradır. 2020-2023-cü illərdə Prezident işğaldan azad edilmiş ərazilərdə 400-ə yaxın tədbirdə iştirak edib, o cümlədən 8 şəhər, 32 kənd və qəsəbə olmaqla, 120 layihənin təməlini qoymuş, müxtəlif təyinatlı 71 tikinti obyektinin açılışını edib”.

Yaşayış məntəqələrinin salınması ilə yanaşı, bölgədə geniş bərpa-quruculuq işləri aparılır: 

“Orta ümumtəhsil məktəbləri, körpələr evi-uşaq bağçaları, xəstəxanalar, mədəniyyət və turizm obyektləri kimi sosial təyinatlı obyektlərin bərpası və yenidən qurulması ilə bağlı müvafiq tədbirlər həyata keçirilir. İnfrastruktur layihələri sırasında Füzuli və Zəngilan şəhərlərində beynəlxalq hava limanları istismara verilib, Laçın rayonunda hava limanının tikintisi davam etdirilir. Həmçinin avtomobil yolları, tunellər, körpülər, dəmir yolları, magistral qaz xətləri tikilir, su elektrik stansiyaları və yarımstansiyalar, su anbarları inşa edilir”.


Ulu öndər Heydər Əliyevin anadan olmasının 101-ci ildönümüdür
10 May, 2024
00:01
1399
390
64

Bu gün bütün türk dünyasının iftixarı, dünyaşöhrətli müdrik siyasi şəxsiyyət və görkəmli dövlət xadimi, müasir müstəqil Azərbaycan dövlətinin memarı və qurucusu ümummilli lider Heydər Əliyevin anadan olmasından 101 il ötür.

Heydər Əlirza oğlu Əliyev 1923-cü il mayın 10-da Azərbaycan Respublikasının Naxçıvan şəhərində anadan olub.

1939-cu ildə Naxçıvan Pedaqoji Texnikumunu bitirdikdən sonra Azərbaycan Sənaye İnstitutunun (indiki Azərbaycan Dövlət Neft və Sənaye Universiteti) memarlıq fakültəsinə daxil olub, lakin İkinci Dünya müharibəsinin başlanması ona təhsilini başa çatdırmağa imkan verməyib.

Heydər Əliyev 1941-1944-cü illərdə əvvəlcə Naxçıvan Muxtar Respublikası Xalq Daxili İşlər Komissarlığında arxiv şöbəsinin məxfi hissəsinin müdiri, sonra isə Naxçıvan MSSR Xalq Komissarları Sovetində ümumi şöbənin müdiri vəzifələrində işləyib.

1944-cü ilin may ayında dövlət təhlükəsizliyi orqanlarında işə göndərilib.

1949-1950-ci illərdə SSRİ Dövlət Təhlükəsizlik Komitəsinin Leninqraddakı (indiki Sankt-Peterburq) Rəhbər Kadrların Hazırlığı Məktəbində təhsil aldıqdan sonra, 1950-ci ildə Azərbaycan SSR Dövlət Təhlükəsizliyi Komitəsində bölmə rəisi təyin edilib.

1957-ci ildə Azərbaycan Dövlət Universitetinin (indiki Bakı Dövlət Universiteti) tarix fakültəsinin qiyabi şöbəsini bitirib.

1958-ci ildə Azərbaycan SSR Dövlət Təhlükəsizliyi Komitəsinin əks-kəşfiyyat şöbəsinin rəisi, 1964-cü ildə DTK-nın sədr müavini təyin edilib.

1966-cı ildə Moskvada DTK-nın F.E.Dzerjinski adına Ali Məktəbinin rəhbər heyətin təkmilləşdirilməsi kurslarını müvəffəqiyyətlə bitirib.

1967-ci ildə Azərbaycan SSR Nazirlər Soveti yanında Dövlət Təhlükəsizliyi Komitəsinin sədri vəzifəsinə təyin edilib və həmin ildə də ona general-mayor rütbəsi verilib.

Azərbaycan Kommunist Partiyası Mərkəzi Komitəsinin 1969-cu il iyulun 14-də keçirilmiş plenumunda Heydər Əliyev Azərbaycan Kommunist Partiyası Mərkəzi Komitəsinin birinci katibi seçilib.

Heydər Əliyev 22 il Azərbaycan SSR Ali Sovetinin və SSRİ Ali Sovetinin deputatı olub. 1974-1979-cu illərdə isə SSRİ Ali Soveti İttifaq Şurasının sədr müavini vəzifəsini tutub.

1976-cı ildə Sovet İttifaqı Kommunist Partiyası Mərkəzi Komitəsinin Siyasi Bürosunun üzvlüyünə namizəd, 1982-ci ilin dekabrında isə Siyasi Büronun üzvü seçilən Heydər Əliyev SSRİ Nazirlər Soveti sədrinin birinci müavini vəzifəsinə təyin edilib. Bu vəzifədə işləyərkən Heydər Əliyev SSRİ-nin iqtisadi, sosial və mədəni həyatının ən mühüm sahələrinə rəhbərlik edib.

Heydər Əliyev 1987-ci ilin oktyabrında Sovet İttifaqı Kommunist Partiyası Mərkəzi Komitəsi Siyasi Bürosunun və şəxsən baş katib Mixail Qorbaçovun yeritdiyi siyasi xəttə etiraz olaraq tutduğu vəzifələrdən istefa verib.

Heydər Əliyev 1990-cı il yanvarın 19-dan 20-nə keçən gecə sovet qoşunlarının Bakıda törətdiyi qanlı faciə ilə əlaqədar, yanvarın 21-də Azərbaycanın Moskvadakı nümayəndəliyində bəyanatla çıxış edərək, Azərbaycan xalqına qarşı törədilmiş cinayətin təşkilatçıları və icraçılarının cəzalandırılmasını tələb edib. O, Dağlıq Qarabağda yaranmış kəskin münaqişəli vəziyyətlə bağlı SSRİ rəhbərliyinin ikiüzlü siyasətinə etiraz əlaməti olaraq, 1991-ci ilin iyulunda Sovet İttifaqı Kommunist Partiyasının sıralarını tərk edib.

1990-cı il iyulun 20-də Bakıya qayıdan Heydər Əliyev iki gün sonra Naxçıvana yola düşüb, həmin ildə də Azərbaycan SSR xalq deputatı və Naxçıvan MSSR xalq deputatı seçilib.

1991-ci il sentyabrın 3-də Heydər Əliyev Naxçıvan Muxtar Respublikası Ali Sovetinin sədri seçilib və müvafiq qanunvericiliyə əsasən, həm də Azərbaycan Respublikası Ali Soveti sədrinin müavini olub. Bu vəzifədə o, 1993-cü ilə kimi çalışıb.

Heydər Əliyev 1992-ci il noyabrın 21-də Yeni Azərbaycan Partiyasının Naxçıvan şəhərində keçirilmiş təsis konfransında partiyanın sədri seçilib.

1993-cü ilin may-iyun aylarında ölkədə vətəndaş müharibəsi və müstəqilliyin itirilməsi təhlükəsi yarandığına görə, Azərbaycan xalqı Heydər Əliyevin hakimiyyətə gətirilməsi tələbini irəli sürüb və ölkənin ozamankı rəhbərliyi onu Bakıya dəvət etməyə məcbur olub.

Heydər Əliyev 1993-cü il iyunun 15-də Azərbaycan Respublikası Ali Sovetinin sədri seçilib, iyunun 24-dən isə Azərbaycan Respublikası Prezidentinin səlahiyyətlərini həyata keçirməyə başlayıb.

1993-cü il oktyabrın 3-də ümumxalq səsverməsi nəticəsində Heydər Əliyev Azərbaycan Respublikasının Prezidenti seçilib.

O, 1998-ci il oktyabrın 11-də xalqın yüksək fəallığı şəraitində keçirilən seçkidə səslərin 76,1 faizini toplayaraq, yenidən Azərbaycan Respublikasının Prezidenti seçilib.

2003-cü il oktyabrın 15-də keçirilən prezident seçkisində namizədliyinin irəli sürülməsinə razılıq vermiş Heydər Əliyev səhhətində yaranmış problemlərlə əlaqədar namizədliyini İlham Əliyevin xeyrinə geri götürüb.

2003-cü il dekabrın 12-də Azərbaycan xalqının ümummilli lideri Heydər Əliyev Amerika Birləşmiş Ştatlarının Klivlend Klinikasında vəfat edib və dekabrın 15-də Bakıda, Fəxri xiyabanda dəfn olunub.

Heydər Əliyev beş dəfə keçmiş SSRİ-nin Lenin ordeni ilə, Qırmızı Ulduz ordeni və çoxsaylı medallarla təltif edilib, iki dəfə Sosialist Əməyi Qəhrəmanı adına, həmçinin müxtəlif ölkələrin ali mükafatlarına, nüfuzlu ali məktəblərin fəxri adlarına layiq görülüb.

Prezident İlham Əliyevin 2022-ci ilin 29 sentyabrında imzaladığı Sərəncamla Azərbaycanda 2023-cü il “Heydər Əliyev İli” elan edilib.



Qərbi Azərbaycan Xronikası: Həm Rusiyanın, həm də Qərbin planına görə, Zəngəzur dəhlizi reallaşacaq - VİDEO
9 May, 2024
23:36
1348
140
11

Qərbi Azərbaycan Xronikası layihəsi çərçivəsində növbəti analitik süjet hazırlanıb.

“Qərbi Azərbaycan reallığı erməni ictimai rəyinə yerləşməyə başlayır” adlı süjetdə Qazaxın dörd kəndinin qaytarılması və sərhədin demarkasiyasının Tavuş istiqamətində başlanmasından sonra Ermənistanda “Qərbi Azərbaycan” mövzusu üzrə müzakirənin intensivləşdiyi bildirilir.

Qeyd olunub ki, bütün bunlar Qərbi Azərbaycan reallığının erməni ictimai rəyinə yerləşməyə başlamasından xəbər verir: “Xüsusilə II Qarabağ müharibəsində qazanılan Zəfərdən sonra onlar anlayırlar ki, azərbaycanlıların tarixi torpaqlarına qayıdışı qaçılmazdır və bununla razılaşmalı olacaqlar. Ermənistanda “Qərbi Azərbaycan” müzakirələrinin əsas səbəbi Qazaxın kəndlərinin qaytarılmasından sonra rəsmi Bakının hansı tələblər irəli sürməsi haqqında səslənən fikirlərdir. Əslində isə növbəti hədəfin Zəngəzur dəhlizinin açılması olduğu sirr deyil”.

Süjetdə bu il aprelin 23-də Prezident İlham Əliyevin ADA Universitetində keçirilən “COP29 və Azərbaycan üçün Yaşıl Baxış” mövzusundakı beynəlxalq forumda çıxışı zamanı Zəngəzur dəhlizi məsələsi ilə bağlı konkret mövqe açıqladığı vurğulanır.

Diqqətə çatdırılıb ki, həm sərhədin delimitasiyası üzrə razılığın əldə edilməsi, həm də kommunikasiyanın hansısa prinsiplərə uyğun açılması variantları Azərbaycan üçün məqbuldur və hər iki variantda dəhliz tələbi yerinə yetirilməlidir: “Bunu anlayan Qərb ölkələri artıq Azərbaycanın mövqeyini qəbul edirlər və əsas strategiya olaraq, Orta dəhlizin açılması seçilib. Bakı-İrəvan danışıqlarının növbəti raundunda ən aktual məsələ Zəngəzur dəhlizinin açılması olacaq. Ermənistanda hesab edirlər ki, bu dəhlizin reallaşması azərbaycanlıların Qərbi Azərbaycana qayıdışının da başlanğıcı olacaq”.

Erməni hüquqşünas Varazdat Arutyunyan, politoloq Beniamin Matevosyan və rusiyalı politoloq Boqdan Bezpalkonun fikrincə, baş nazir Nikol Paşinyanın gündə bir neçə dəfə “legitimlik” sözünü işlətməsi Azərbaycanın tələblərinin icrasının qaçılmaz olduğunu izah etmək məqsədi daşıyır: “Azərbaycanın növbəti hədəfi Sünikdən (Zəngəzur) dəhliz əldə etməkdir və Türkiyə də bu planı sona qədər dəstəkləyir. Ermənistan daha dəhşətli ssenari ilə üzləşəcək. Belə ki, Ermənistan cənubdakı əraziləri itirəcək. Bununla Zəngəzur dəhlizinin keçəcəyi bölgəyə Azərbaycan nəzarət edəcək”.

Sonda vurğulanıb ki, baş verənlər bir xəbərin müjdəçisidir: “Qərbi Azərbaycana addım-addım yaxınlaşırıq”.

Xatırladaq ki, Qərbi Azərbaycan Xronikası layihəsinin məqsədi tarixi qədim torpaqlarımızın adının yaşadılması, tanıdılması, həmçinin azərbaycanlıların ermənilər tərəfindən deportasiyaya məruz qoyulmasından, həmin ərazilərdə mövcud olmuş, lakin adı silinən toponimlərin, saysız-hesabsız yeraltı və yerüstü maddi mədəniyyət nümunələri - qədim yaşayış məskənləri, nekropollar, kurqanlar, qala, saray və istehkam qalıqları, karvansaralar, körpülər, qəbirüstü sənduqələr, xaçdaşlar, at-qoç heykəlləri, məbəd, kilsə, məscid, pir və ocaqların üzə çıxarılması, həmin ərazinin təmiz oğuz-türk məskənləri olduğunu təsdiq edən faktların dünya ictimaiyyətinə çatdırılmasıdır.

Həmçinin Prezident İlham Əliyevin Qərbi Azərbaycanla bağlı dediyi “XX əsrin əvvəllərinə təsadüf edən xəritə bir daha onu göstərir ki, Qərbi Azərbaycan tarixi Azərbaycan diyarıdır, şəhərlərin, kəndlərin adları Azərbaycan mənşəlidir və biz yaxşı bilirik ki, indiki Ermənistan ərazisində tarix boyu Azərbaycan xalqı yaşayıb. İndi əsas vəzifə ondan ibarətdir ki, dünya ictimaiyyəti də bunu bilsin”, - fikrini əsas tutaraq Qərbi Azərbaycan İcmasının hazırladığı Qayıdış Konsepsiyasından irəli gələn vəzifələrin təbliğidir.

Bundan əlavə, Qərbi Azərbaycanla bağlı tarixçilərin, araşdırmaçıların düşüncələrini, deportasiyaya məruz qalmış şəxslərin həyat hekayəsini işıqlandırmaqdır.

Daha ətraflı Baku TV-nin süjetində:

Həzi Əhəd oğlu Aslanov 1910-cu il yanvarın 22-də Lənkəran rayonunun Gərmətük qəsəbəsində doğulub.

13 yaşında atasını itirən Həzi ailəsinə baxmaq üçün bir müddət kərpic zavodunda fəhlə işləyir, daha sonra isə Zaqafqaziya hərbi hazırlıq məktəbinə göndərilir.

O, hərbi hazırlıq məktəbində oxuduğu zaman qısa müddət də olsa, məktəbin “rota qəzeti”ndə redaktor kimi işləyir. 1937-ci ildə Ukrayna SSR-in Obruç şəhər sovetinin deputatı seçilən Həzi Aslanov İkinci Dünya müharibəsinə qədər sovet ordusunda bir çox yüksək vəzifələrdə çalışıb. Stalinqradın azad olunmasında sərkərdə Həzi Aslanovun müstəsna xidmətləri olub. O, 32 yaşında Sovet İttifaqı Qəhrəmanı, 34 yaşında isə general olub.

1945-ci ildə bütün müttəfiq respublikalarda müdafiə nazirlikləri yaranan zaman Mircəfər Bağırov onu Azərbaycanın müdafiə naziri təyin etmək haqqında fikir bildirir. Həmin vaxt Nazirlər Sovetinin sədri olan Teymur Quliyev deyir ki, hazırda müharibə gedir, Həzi Aslanova icazə verməzlər, o döyüşdədir.

Bağırov Stalinə zəng edib, Həzi Aslanovun Azərbaycana gəlməsi üçün icazə alır. Onu ilk təbrik edən SSRİ hərbi rəhbərliyində təmsil olunan erməni generalı Baqramyan olur. O, Həzi Aslanova deyir: “Həzi, səni təbrik edirəm, sən sabah Azərbaycan Kommunist Partiyasının sərəncamına getməlisən, səni Azərbaycana müdafiə naziri təyin edirlər. Ancaq sabah biz hücuma hazırlaşırıq. Mən istərdim ki, sən özün hücumu planlaşdırasan”.

Həzi Aslanov təklif edir ki, almanlardan qənimət götürülən altılüləli minomyot orta cinahda yerləşdirilsin və düşmənə atəş açsın. Səhəri gün Həzi Aslanov Bakıya getməli idi. Onun bir yük maşını var idi, dincəlmək üçün həmin maşını yaşayış otağına çevirmişdi. Oraya gedir, çəkmələrini çıxarır ki, rahatlansın. Aradan 20-25 dəqiqə keçməmiş altılüləli minomyotdan çıxan altı mərmi Həzi Aslanovun olduğu maşına dəyir.

General Həzi Aslanov 24 yanvar 1945-ci ildə Mitava şəhəri yaxınlığında müəmmalı şəraitdə həlak olur. Ona ikinci dəfə Sovet İttifaqı Qəhrəmanı adı ölümündən 47 il sonra, 1991-ci ildə verilir.

Daha ətraflı Baku TV-nin süjetində:

Şuşa sakinləri doğma yurdlarına köçməyə hazırlaşırlar - Xəbərlərin 20:00 buraxılışı
9 May, 2024
20:00
809
112
8

Baku TV-nin canlı yayımında xəbər vaxtıdır.

Faşizm üzərində tarixi qələbədən 79 il ötür. Prezident və Birinci xanım Qələbə uğrunda həlak olan azərbaycanlıların xatirəsini andılar.

Malıbəylidə insana məxsus sümük fraqmentləri aşkarlandı. Baş Prokurorluq məlumat yaydı.

Şuşa sakinləri doğma yurdlarına köçməyə hazırlaşırlar.

Hoteldə zəhərlənənlərin yaxınları Baku TV-yə danışdılar.

Təmirdən sonra yolda yaranan yarıq sürücülərə çətin anlar yaşatdı. Bir gecədə 10 maşının təkəri partladı.

Daha ətraflı BAKU NEWS-un 20:00 buraxılışında:

"""


olusan_metin = encypt("""“Şuşada seysmoloji stansiyanın qurulması ilə bağlı işlər başa çatıb. Orada abadlıq işləri və stansiyanın quraşdırılması işi qalıb”.
Oxu.Az xəbər verir ki, bunu jurnalistlərə açıqlamasında AMEA nəzdində Respublika Seysmoloji Xidmət Mərkəzinin baş direktoru Qurban Yetirmişli deyib.
O bildirib ki, bu stansiya Türkiyənin AFAD qurumu tərəfindən bizə hədiyyə edilib.
“Bu, Azərbaycanda 4-cü quyudibi stansiya olacaq. 100 metr dərinliyində yerləşəcək. Bütün azad edilmiş ərazilərdə kompleks tədqiqatlar aparacağıq”.
O qeyd edib ki, növbəti quyudibi stansiya Cəbrayılda tikilməlidir.""")



genel_frekanslar = {}
for a in harfler:
	genel_frekanslar[ a ] = genel.count(a)


countlar = list(genel_frekanslar.values())

def toplam( l: list ) -> int:
	toplanan_deger = 0
	for number in l:
		toplanan_deger = toplanan_deger + number
	return toplanan_deger


sonuc = toplam(countlar)
print(sonuc)


for a in harfler:
	genel_frekanslar[ a ] = round(genel_frekanslar[ a ] / sonuc, 4)


print("genel_frekanslar", genel_frekanslar)


print(olusan_metin)


sifre_frekanslar = {}
for a in harfler:
	sifre_frekanslar[ a ] = olusan_metin.count(a)


sonuc2 = toplam(list(sifre_frekanslar.values()))
for a in sifre_frekanslar:
	sifre_frekanslar[a] = round(sifre_frekanslar[a] / sonuc2, 4)

print('=================')
print(sifreleme2)
print(genel_frekanslar)
print('')
print(sifre_frekanslar)







sys.exit(1)
# =============================






#encypt( "test" )



sys.exit(1)

#range(4) ==> 0, 1, 2, 3
#range(2) ==> 0, 1
#range(N) ==> 0, 1, ,...... N-1









# If there are more than one lines of text in a string data, use """ instead of "
inputtext1 = """Azərbaycan xarici işlər naziri Ceyhun Bayramov Qazaxıstana işgüzar səfərə yola düşüb.
Bu barədə Azərbaycan Xarici İşlər Nazirliyi məlumat yayıb.
Səfər çərçivəsində Almatı şəhərində Azərbaycan və Ermənistan xarici işlər nazirlərinin iki ölkə arasında “Sülhün və dövlətlərarası münasibətlərin təsis edilməsi haqqında ikitərəfli Saziş” layihəsi üzrə danışıqlarının növbəti raundunun, habelə Qazaxıstan baş nazirinin müavini, xarici işlər naziri ilə görüşlərin keçirilməsi nəzərdə tutulub.
"""




inputtext2 = "Azərbaycan xarici işlər naziri Ceyhun Bayramov Qazaxıstana işgüzar səfərə yola düşüb.Bu barədə Azərbaycan Xarici İşlər Nazirliyi məlumat yayıb.Səfər çərçivəsində Almatı şəhərində Azərbaycan və Ermənistan xarici işlər nazirlərinin iki ölkə arasında “Sülhün və dövlətlərarası münasibətlərin təsis edilməsi haqqında ikitərəfli Saziş” layihəsi üzrə danışıqlarının növbəti raundunun, habelə Qazaxıstan baş nazirinin müavini, xarici işlər naziri ilə görüşlərin keçirilməsi nəzərdə tutulub."


print(inputtext1)
print("=====================")
print(inputtext2)



i1 = """
a
b
c
"""

i2 = "a b c"

print("==============")
print(i1)
print(i2)



a = "Ahmet"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])


print(a[0:3])
