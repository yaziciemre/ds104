import operator

# 1 load data from file or value directly
# 2 find the words in text, find the frequency of words
# 3 calculate the length and frequency gain of each word
# 4 sort the words by gain
# 5 make short form of words
# 6 replace the words with short form
# 7 save the data to file

# 1
text = "Hazırda ölkəmiz dünyada neokolonializm meyllərinin qarşısının alınması, bu siyasətin qurbanına çevrilən xalqların səsinin eşidilməsi istiqamətində də fəal siyasət yürüdür. Prezident İlham Əliyev Forumdakı çıxışında bu məsələyə də ətraflı toxunub. Onun sözlərinə görə, Qoşulmama Hərəkatının üzvlərinin əksər hissəsinin çox ağır, qaranlıq müstəmləkə tarixçəsi olub və buna qarşı mübarizənin aparılması o deməkdir ki, biz buna inanırıq: “Çünki biz ədalət naminə danışırıq, çünki biz beynəlxalq hüquq naminə danışırıq. Yəni, biz belə bir məsələyə imkan verə bilmərik ki, indi - XXI əsrdə bəzi Avropa ölkələri digər xalqlara müstəmləkə kimi yanaşsın. Təbii ki, biz öz səsimizi ucaltdıqda, Hərəkatda sədrliyimiz zamanı bu məsələni qaldırdıqda bu, onunla bağlı deyildi ki, biz hansısa ölkələrə qarşı idik. Biz, sadəcə, ədalətə, beynəlxalq hüquqa bağlı idik. Bu, yaddan çıxmalı deyil. Dünya məcburi assimilyasiyaya aparan belə bir iyrənc neokolonializm təcrübəsinə göz yummamalıdır. Ondan çox fransız dənizaşırı ərazisində həyata keçirilən məcburi assimilyasiya əsla qəbuledilməzdir və buna son qoyulmalıdır. Bu səbəbdən Avropa təsisatları bəzən çalışırlar Avropada olmayan ölkələrin daxili işlərinə müdaxilə etsinlər. Amma Avropa Parlamenti və AŞPA bununla bağlı səsini çıxarmır. Çünki yeni müstəmləkə tendensiyaları yenə də davam edir. Onda siz nəyə görə tənqid etmirsiniz? Nəyə görə siz sanksiyalar tətbiq etmirsiniz? Nəyə görə susursunuz? Bəli, biz sədr olaraq Hərəkat daxilində bu işi gördük”.  Ölkəmiz bu il daha bir möhtəşəm tədbirə - COP29-a ev sahibliyi edəcək. Sülh və sabitliyi, dialoqu şərtləndirən iqlim dəyişmələri kimi beynəlxalq səviyyəli aktual bir problemin təfərrüatları, həlli yolları Bakıda müzakirə olunacaq. Forumdakı çıxışında bu məsələyə də toxunan Prezident İlham Əliyev bildirib ki, maliyyə məsələsi COP29-un əsas mövzusu olacaq: “Lakin bizə həmrəylik və qarşılıqlı etimad lazımdır. Biz bir-birimizi günahlandırmalı deyilik ki, kim planetə daha çox zərbə vurub. Yaxud da qlobal istiləşməyə görə kimin daha çox məsuliyyət daşıması ilə bağlı mübahisə etməməliyik. Əgər biz bu davranışı davam etdirsək, onda bunun sonu faciə olacaq”. Dövlət başçısı bildirib ki, bizim yaşıl gündəliyimiz var və biz buna COP29-a ev sahibliyi etmək şərəfinə layiq görüləndən xeyli əvvəl başlamışıq: “2027-ci ilə qədər bizdə 2 qiqavat Günəş və külək enerjisi stansiyaları işə düşəcək və 2030-cu ilə qədər əlavə 5 qiqavat da istismara veriləcək. Bunun sayəsində bərpaolunan enerjini elektrik enerjisi istehsalında istifadə etmək üçün bizə imkan yaranacaqdır”. Lakin Ermənistanda son günlər bir sıra təxribatçı qüvvələr iki ölkə arasında qalıcı sülhün əldə edilməsinə töhfə verə biləcək sözügedən razılaşmanın icrasına mane olmaq üçün var gücü ilə çalışırlar. Çox narahatlıq doğuran haldır ki, həmin prosesləri Erməni Qriqorian Kilsəsinin dini xadimləri fəal rol alıblar. Sözügedən din xadimləri siyasi tələblər irəli sürür, Azərbaycanla sülh əldə etməyə qarşı çıxır və aşkar şəkildə revanşa və müharibəyə çağırış edirlər. Bu gün dünyada mədəniyyətlərarası dialoqun təşviqində, sülh və sabitliyin təminində əsas amillərdən biri də təbii ki, çoxtərəflilik prinsipidir. Azərbaycan bu prinsipi çox uğurla tətbiq edir. Biz bunun Bakının Qoşulmama Hərəkatına sədrliyi dövründə də əyani şahidi olduq. Prezident İlham Əliyevin də vurğuladığı kimi, Azərbaycan öz təcrübəsini göstərib: “Biz qəti şəkildə çoxtərəfliliyə sadiqik. Biz çoxtərəflilik dəyərlərini 120 ölkənin üzv olduğu Qoşulmama Hərəkatında 2019-cu ildən bu ilin əvvəlinə qədər təşviq etmişik. O, BMT-dən sonra ikinci ən böyük təşkilatdır və həmçinin bununla bağlı yekdil qərarımız oldu, sədrliyimiz yekdil qərarla əlavə bir il də artırıldı. Təbii ki, Qoşulmama Hərəkatının vacib təməl dəyərləri məhz suverenlik, ölkələrin ərazi bütövlüyü, daxili işlərə qarışmamaqdır. Biz həmin Hərəkatın təsisatlanması seqmentinin gücləndirilməsinə çalışdıq və bununla bağlı daxildə şəbəkə yaratdıq, qadınların və gənclərin təşkilatlarını təsis etdik. Bütün bunlar məhz Azərbaycan tərəfindən yaradılıb. Əminəm ki, Qoşulmama Hərəkatının təsisatlanması istiqamətində inkişafı gələcəkdə də davam edəcək”. Qeyd edək ki, hazırda dünyada müxtəlif etnik, milli, dini və siyasi kataklizmlərin yaşandığı məqamda belə bir Forumun təşkili Bakının dünyaya sülh və dialoq çağırışı kimi qiymətləndirilir. Müharibələr və münaqişələrin artdığı bir zamanda Azərbaycan bu sahədə özünün əsrlərə dayanan münbit təcrübəsini dünyaya təqdim edir. Prezident İlham Əliyevin Forumdakı çıxışında əsas vurğulardan biri də məhz bu məqam idi. Dövlət başçısı bildirib ki, əsrlər boyu Azərbaycan mədəniyyətlərin qovuşduğu məkan olub. Bizim coğrafi mövqeyimiz, Şərq ilə Qərb arasında yerləşməyimiz, əslində, bu tendensiyaya imkan yaradıb: “Çoxmədəniyyətli və böyük etnik müxtəlifliyə malik olan Azərbaycan cəmiyyəti əsrlər boyu ən mühüm dəyərləri - tolerantlığı, qarşılıqlı hörməti, dostluq və tərəfdaşlıq kimi dəyərləri qoruyub. Əminəm ki, bir müstəqil ölkə kimi Azərbaycanın uğurlu inkişafını şərtləndirən məsələ məhz bunlardan ibarətdir. Azərbaycanda yaşayan insanlar, müxtəlif etnik qrupların və dinlərin təmsilçiləri bir ailə kimi yaşayırlar. Onlar Azərbaycanın dəyərli vətəndaşlarıdır, dövlətimizin, dövlətçiliyimizin əsl vətənpərvər insanlarıdır. Biz bu müsbət tendensiyaları, bu mədəni dialoqu, mədəni müxtəlifliyi gücləndirməliyik və əlbəttə ki, bütün bunlar bir çox əsrlərdən gələn nemətdir”. Azərbaycanın Ümumdünya Mədəniyyətlərarası Dialoq Forumuna ev sahibliyi günlərdə Erməni Qriqorian Kilsəsinin sülh əleyhinə fəaliyyəti təəssüf doğurur və çoxlu mətləblərdən xəbər verir. Qeyd edək ki, azərbaycanlıların Ermənistandan qovulmasında və Ermənistanın Azərbaycana qarşı hərbi təcavüzündə Erməni Qriqorian Kilsəsi xüsusi fəallıq nümayiş etdirmişdir.Qərbi Azərbaycan İcması beynəlxalq ictimaiyyəti və dünya dini liderlərini Erməni Qriqorian Kilsəsinin həmin əməllərini pisləməyə və Azərbaycan və Ermənistan arasında davamlı sülhə dəstək verməyə çağırır."

# 2a
# "these are words"   ⟶   ["these", "are", "words"]
words = text.split()

# 2b
frequencies = {}

for word in words:
    frequencies[ word ] = 0

for word in words: 
    if word in frequencies: 
        # If the word has it been seen before, increment
        frequencies[word] = frequencies[word] + 1
    else:
        # If the word has not been seen before
        frequencies[word] = 1

# 3
gain = {}
for word in words:
    gain[word] = frequencies[word] * (len(word) - 2)

# 4 
sorted_d = sorted(gain.items(), key=operator.itemgetter(1), reverse=True)

# 5
n = 20
# get the top n items from gain
shortform = sorted_d[ : n]

print(shortform)

# 6



# All of them below are same
# ===============
mydict = {
    'Ahmet': 29,
    'Ali': 30
}
mydict['Pelin'] = 25
# ===============
mydict = {
    'Ahmet': 29,
    'Ali': 30,
    'Pelin': 25
}
# ===============
mydict = {}
mydict['Pelin'] = 25
mydict['Ali'] = 30
mydict['Ahmet'] = 29

