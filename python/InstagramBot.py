from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint


class InstagramBot:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('D:\Projeler\Instagram Çekiliş Botu\chromedriver.exe')
        self.username = username
        self.password = password
        self.etiketListesi = ["xq_onur_h_xq", "fuatyasugey", "nahitbult00", "m.eminn.45", "mirac_sevderogluu23", "nahid_011_", "__hu45yin_grbz__", "papatyam.1144", "34ceyhn.asln", "cafersaridaq", "nezihpalaz", "adileyuksell", "mahmut.savas1235", "umit_bkrr__", "bysemihsen", "osmanalptekin21", "elanurtarhan07", "seval_bcakc_09", "tubadmz", "bbusesar", "devrancomert00", "siyah_incii.34", "19_08_2020", "_m._celik35", "basri_374", "ridvankrts_", "nazmi_akyurek", "sihh_costta", "welifgunbey", "__dicl3", "ahmetkahya.54", "sematlslii", "emre_gdx", "kaan_bln00", "bm.da._dawid", "barinayisik", "mag_azinhaber", "guneykuzey20", "studddyyyblogsssss", "asli_harikasii", "karakasv__44", "mzahd_12", "kaan.erol76", "whenbroken", "hamza_altundag63", "wesra.kayaa", "ksr_zyp", "sero.yapim", "hatice.badr", "m_enes_25_", "blt.tugba51", "esrakaaplann", "_orhanakyelll_07", "p_a_t_r_o_n__004", "lavanya21.2", "hamza_sanler", "b.sayin69", "nazipek.35", "mizahbombs", "aksyhsyn21", "rukenkartal.2121", "yinemizahlandik", "dsagbirge", "m.soylsnx16", "demircirem03", "batuhan.baser.1903", "kadiruzuner11", "guzel___sozleri", "_elham_i", "eda.0392", "nuriclk.3457", "xd_halil_xd", "serkn_kandemir", "muham.met.58.58", "aybuke._.08", "hocamyarenucyiyio", "ecen.urr", "batuhankavalci_", "can.kara27", "ferau_lina__", "hcanmert", "eglenceli_tabak_tarifleri", "erenkinkg", "osmanerturk66", "elifuslans", "esra.kyuncu", "xo.160__", "aleynakalkann_1", "mardinvideo.47", "professional_illustrator.ela", "falco_num", "onderhamza", "kesgiin.x", "tugceogus", "emirinkeki_yedek", "oriflame_elifs", "meyra.bal", "kasikci_dede_cigkofte", "emrullahaydin4949", "alicabir_", "keskinfurkan_", "dogu_aygul", "m.f_yaman", "eda_petekk", "aslihanbulutdemirezen", "sinan_387vrcn", "mehmed.4848", "ebrar_018", "baahhy", "idris_arac", "eda._yalcinkaya.2", "bayramgozcu06", "00__didemm", "_pw.dmll", "esra.yalinn", "nurlan.ff_", "ertem.mehmet44", "burakkoseofficial", "melikdiler00", "1986ekremofficial", "demetakalinn0", "alican_mtnx", "slslxmdk_jxmmx", "evin_sns", "ekremalgm", "_someoneunidentified", "komiklerin50tonu", "iremborhannn", "memet.arslnn", "dilekertekinbaykal", "kemalozsaka35", "_hilalsrerrrr", "alya_butik7", "yusra.sarikaya23", "shrpulat", "umutkodaman7", "_senin_hayalerin_", "keremcan1456", "kartanesifm06", "tomris659", "ersel931", "azad_aydar", "sena_aydin_1903", "tugbarecepotguc", "96_temo", "msukrumuslu", "elanur_yalcin_13", "yuse.roje", "m99mer", "zleyha_colakk1", "furkan.yilmazogullari", "video.sokagi21", "baverkan21", "burrakk_119", "wiosv", "mubisblog", "ahzem1722", "farmasisevgi02", "diiyar_", "mustafaparlak25", "kubr.kc", "oktay_busra_bkr", "huzunlu__poncikkkk", "du.rsun1910", "knk.nurullah", "minefashionlab", "arda_x_sezgin", "deniz_b14", "sima.soma.758", "sananeoyol", "malikcelik6565", "_tugce_balkan1", "bahaar_oztekn", "emin_trhn.4747", "bugra.aslan53", "mert_.can06", "cihan.akyurt", "abdulaevv134", "melek_bzdmrr", "melis_dlk", "16bsrbrs", "hasangunay_", "mervekarakaya85", "kubilay.atayy", "halilyildiz1676", "sevinc_khudueva", "berra.iremdmr", "cerens.diarys_yedeks", "ekrem.orj27", "tikktokfan", "mubeyyen_kacar", "semihcanckm", "erdemakse", "bakkalogluyusuf", "barankaya2101", "zeynepcelepci06", "cellatinkizlari_prensesleri36", "f5rkaan", "muhammet.tsdmr34", "yusuf_yuce3870", "esenakyuzz", "helin_inci.271", "ataturkm655", "xnur_64", "ukala.kiz51", "icinizdenbirii47", "arsln.sedat", "merdoderdo_", "senassyn", "salihhoca39", "tuana.acar.142035", "ysf_aydn35", "savrankorkmaaz", "nykwildriftmontaj", "04mehdimns", "furkanozarslan8", "ali.ozbekkk", "aysekurem.49", "tarik_dertlioglu", "furkann.01_", "r4fe7", "31.xestesi", "beyzatakac", "ahmetanarr", "yusuftaha4206", "sevdaaktrl", "dil___34", "haluk_demirr", "eliabdullayev.207", "tunc.ay7452", "tuba_crknt", "abdullah.oktayy", "ferdisahin__", "hasan_arslan_43_43", "gurr_alper", "sefa_oksuz_", "hrstkara", "_dilo_priw", "senanrakts", "lutfensakinnles", "dogan__askan", "levent_gunesgormez", "hilmi.aksy", "ponciklendiniz.789", "gurbanovn999", "dgrmnc677", "cemil_cnar4242", "ilknur.dogan_", "ayhan_krts01", "basmaya.abdulkadir", "latyf_1", "ahmetaydn1628", "_xq.koray.xq_", "yasinkocc2k", "muhammedckr5672", "ardahzr.33", "furkanyildizli001", "ben_sana_yandim_deli", "sibel_yalcinnnn", "eshqbil", "grkngamzeusta", "embracehumanity1", "sude_45_3", "senermerve._", "kevser_ozeen", "musa_oskay", "melikeaktimur", "selenncotenn", "dilhunbirkul", "alituran61.5", "_ilknuurr_d", "ismail_elak", "dash__vortex", "edaky_a", "bilinmezadammx", "some_psychological_issues", "srvtakc_02", "nfttc", "aesthectic_builder", "donaykeskin87", "yusuf._.cobanlar1", "mankurt_54", "alparslan.galatta", "lezzetli_tariflerce", "sevda03.11", "omer20135", "ummuhan.6", "mizginbenli35", "f.bskrt73", "mervegogal", "huseyin.al.001", "senaa.cakar", "avengeekrs", "brknzlcn19", "sumusun_priws", "bayramali.boga", "ahmet_safak17", "xq_good.devil_px", "tugbagerezz", "behzatkara_", "mehmet_deniz_inci80", "zafakurt", "esmira_zeynalli_2015", "eyyupyabir", "sozuygarligi", "hasanarican44", "slxsozdiyari", "sabri_karatas27", "yamanceylinnaz", "aliidb._", "tulayddemez", "zeynepg_12", "sinan__aluc", "mahmut_eminn1", "_qarabg_pg_", "huseyin_cakirhan10", "x_ramocan21", "hmzatyyrchntrzi1903", "ellyhsyeta", "mazlum_aykut_", "chaine_people", "beyza_mcf", "tahaakbulut20", "sajadsamirr", "karsuu.m", "ercan_1234458", "atajan_2707", "sedasevileenn", "muzaffersahindas", "ahmetemir421", "deryademirgulbas", "1osmanc", "sanlihulya68", "asikiz.28", "musa_erdem5621", "xydhckgi", "idonunkanali", "netlugart", "yetkin_hilaloglu", "selinykeli", "elify2468", "elifeda_14", "kader.evlndi", "sedef.uu", "burak_leyjon", "xx_omerfaruukk_xx", "x.rumeysaqx", "hamza_ozdemr", "ayse_gurpinarr45", "seherr_cevikk", "harun.kurun_", "deniz06256", "ceren.isikk_", "meltem_uzz", "alperendurak_2323", "tadi_damagimda11", "hacer_yldrm51", "rafet.efe.gokdemir_01", "abdi_bozkurtx", "burakiftaryilmaz", "ates2alev", "nassk20", "muhammedalmosa", "ozcanbulutbeyaz", "samet.offical6", "gocer_feyza_", "ncyyaran", "ubarancinar", "_iamtugba", "emiryasir1907", "ebubekir_aksuoglu", "dilekyagc", "geri_takip_sayfasi52", "mahsum_okcu", "richbillofficial_page", "unicorn_boy_efe", "ejderyan_", "krmzadee8", "__umut_can_72", "muhammedzaferdinc3304", "klc_ebrux", "nilazuder", "catinmurat21", "murat_demr0", "recai.kadir", "zehra_yngl", "mustafafeyat_", "bukuberry", "uzeyir_orman_02_33", "ridvanomergkmen1903", "autopleinvijftig_cv", "burakelicatal", "safiyesss", "rajput_mitali_4", "mutfaktaki.tatlar", "omertlb", "wesmaisik_", "selcuk.tuncl", "okansilak", "avsaroglu_secil", "recep.tutus", "morteza.gholinejad1", "bulent_sisman_09", "selam_benkardo", "gozde.nrhayatt51", "aysenurogus6", "serrhat_61", "cangl.06", "ebruertekin_", "aliduygu.yildiz", "sevenlerimizinhediyeleriburada", "haticek38", "kjjdjdjfh", "resul_cakr", "yakamozzan", "yarensoydan35", "ktss_yusuf", "mertcan.gebes59", "gucuyener5.2.0", "gt_hane_1", "mahmut8seda", "xx1903mami", "aysekavakfarmasi", "ramo.news", "nursena_basturk", "emrebrht", "yusufertrk_02", "mehmetcan.erdenn", "merve3482020", "m.tunahantoklu", "arehopes", "batunizmx", "gudz0605", "sude.naz5oo", "vie_tnam123", "gsmov.313", "monaqrosaa", "merkurkedisii47_", "9.sinif_ders_pitircigi", "snts_63", "kubos_ask21", "akmanbirol88", "ebranurxbeyzanurr", "fq.fatih", "tansudanoneriler", "ahmet.ozkan25", "_furkankse1", "neset.yilmaz0", "halleeciikk", "serkan_tatlibulak", "irem_0144", "eliifyanar", "nuriyenisagok", "_lord_enzhel_", "ceydakac", "fidanalievaaaa", "gt_sayfasi_042", "ebrusanalnn", "maydanoz_kafaa", "semti.cumuhriyet", "kolge_qara_gunes", "mehmedtut", "mirzaberzan", "esmerbela.1998", "halepli_efe", "etyog", "f.dadass", "hirabkts1834", "zisan.zsn", "mrblr.cnm", "yigittr77", "sultan_gunduz47", "xce911", "by_ali3333", "denizz.yasar", "ksslnn.21", "emperormizah06", "pasa.tepe", "havin_tektas.9", "semayd_", "sensiznotalarr", "fulletentaktikler", "the.elifff", "melisa.brendly", "_azraselvi", "k.mehmetakif_", "samet_official02", "lomexin", "sensedimm_", "renac6792", "mohammed_saiq12", "m.erogluu", "peruze_", "hasansimsek65", "zarok.veli", "sedatsubasi49", "cagriguven6", "habip_subasi_", "_.tukendimm_", "tacsizkiral346", "oyku.qwe", "trkarahan", "1zeynepozturkk", "aylinsonmezx2", "mevlut_efe_ornek", "yarenim5181", "doganonlinee", "serap_akpinnar", "kazanicam28", "murat._.1838", "anil.demrbas", "_ssfa_6", "gizemmiskal", "ff_no_sikinti", "shiny_sunshine1", "serkanaatkn", "aykutkeskxn", "melek.47210", "nouhalaghrib", "resul_mat__", "mrs.nayman", "fkll.all", "bilal_yldrm.72", "crazymotovloq", "alaaddinklkn", "_hus3ynzade_06", "_kubraa_77", "alifrtt_", "betul_danix7", "cankaratas___", "157kilometre", "r0izyy", "raad_altimimi", "halildgci", "halim.88", "nazli_cekil8", "zeliha_cimis", "ceyhun.045", "adanur_sema", "mavikuus", "eskinutku", "sudek0rkmaz", "berkbasarann41", "x.x.ikusursuzanill.x.x", "onlarinmentalitetii", "eyp133ergin", "47_azat_47", "tnahz", "yk60ank", "elifsylvaine", "batuhan_yagmrulu", "ulusoy3824", "furkandenizkoyun", "eeda_nuurr", "i.ftm33", "merylilbae", "xxaysegulxx0606", "x.neslihann.x", "hasn_demr", "omerfarukarslan_", "admino_124", "farukk.tpts", "xq.musabdr.qx", "eda30.06", "ygtovck", "di_lara7604", "ceydacbnkrky", "muhammedtasyussuf", "turanordusu79", "selim.nesil", "sancar_3401", "king_general21", "elmira.pmpgl", "yzcthsn", "serge.n58", "reslblg", "enesibis07", "pierrecardin_uyeligi", "_ramazn.klskr636", "hilaldabanli", "hjgkvcjcgjcgh", "seymaesen925", "helalim5151", "tumblrbirgirlx", "mehtapkarakass", "yusufdalkirdan28", "silasilasilaaaaa", "yigit_enes23", "_hqtice.__", "efkarmedia", "oldbutgoldvinelar", "edasociall", "ra_is_hamou1", "mervantastekin", "enesguness555", "emir_ebinc", "erl.ays", "mehtap.karabulut.3720", "ogulcan.oksas", "queenshhe", "alidogn06", "nurrrrtugba", "emir.ozdal21", "_askbirtutam", "foodie.candyy", "bahar0yalcin", "aliatakandincer", "smrykrgn", "halilcan.tprk", "ferhatnky16", "fincantakim24", "llduygu0l", "bseyyaar", "amine.gucl", "serminocbe", "lnisaa_", "yunusemreergin6", "mert_duramannn", "marjosaci8", "buseyim1", "beki.r4160", "muminesarigullu", "seymagltpe", "mustafaaslan794", "alii.key", "hadisefans.club", "ilknuraygn00", "_suatali", "elifckk58", "sumeyyefarac", "omer_cvsx", "kbra.kurtulus", "_arif_simsek_", "privatepluss", "beyzabakunin", "pdrolog", "tarik.gazi.selcuk", "furkantumx", "ilkayy54", "nuray19o3", "mehmetyildiz8285", "mandaciarda", "memo_can_dyb", "sametturkmen187", "fenerbahcem_ahmethak", "sadiye_saritas", "ftm.yyl", "gemicibekir", "sulosafa", "nusrettin.47", "_vahap_acikgoz_01", "313.ibrahimlii", "_mervee_007", "emreozlem0202", "selinnn_21_", "celikk_tlg", "irmakbaserrx", "esslemcakmak", "scanerkan_", "dermanklg1x", "arslannacelya", "_cansuckrr", "melikekilic173", "tastyytastess", "ll_.zhala._ll", "bbabyyodaa_", "sarpyilmaz525", "ali_muratt", "voguz0", "ts_haber_1", "yagmurceritli", "cumaliilhan1251", "selimdinckal", "m.furkan_7728", "av.birgulaksoy", "_nurcan28", "azat.7300", "ffurkannerginn", "1_minik.mucizem", "yagmurr.erdmm", "mo.art.on", "yelizyldrk_", "aslanmet26", "murat_ylmz.49", "ex.potech", "tubaktemur", "ismail__cannnn", "xkartalice__", "ermanturfan", "keeytootv", "gerroertogan", "nailsbetul", "emin_ozkan_wq", "_tugce.kara_", "mehmet_x_official", "uuryldrm55", "ngrdundar", "elifftxq", "yesim_alkin", "sansiro_parfumeri", "glnr.dd", "yngnsevde", "qz_yunus_qz", "ebincyalcin", "gozde.karaca34", "cuwan_yrlm", "melek_trkmn01", "mustafa060672", "halil.demir.3463", "ismailoran60", "yasemingurlerrr", "sude_zht", "cengizmamedov4", "fat.ma.01", "yunusgoktas5858", "zubeyde_aydogduu", "mert_ocakci", "ekaratasss1", "damla_tmkyy6", "derinhazal.1417", "_yyagmursrc1", "cagrimrtt", "korkmaz_hayrunisa", "ftna78", "burcuaylak", "ahmetcsqs", "nursevim_buldur", "sinan.kntt", "gul.clhaa", "ates1alev", "turan_ygbsn_01", "berkay.ulusuu", "iremmay876", "_kadir_63_27", "beyzqrn", "hidayetofficial47", "nuran.oztrs", "anilkms_", "cuma_boz_27", "fatma.dinler7", "eliff.nurr4", "aslasl909", "razorckls", "mrtrsln1234", "mustafaclk_3373", "kirgin.cicekk51", "devilsutter302", "gulnurumsuu", "igne.dunya", "deryak2748", "zeynep.quenn", "mehmetdagdelen284", "karatut_46sadi", "kullanilmiyor1.27", "oznrylmz5", "sukru_sukru_48", "mutalipakgoz", "l.yasemin.l", "veley7898", "emrahaydemir2002", "selmaaaadgn", "i6raahim", "abdurrahmannx", "ecrinfax", "sengulhosgorr", "sal1h.c", "dilarakocaslannn", "ruhsuz_atmaca.blog", "aliste_arda", "gizemylmaz3555", "muhammetakyz", "helinkaya09", "tcalicanusta", "benhalele.16", "alik.tx", "mertalikus00", "emirhan_becerik", "frsymn77", "omr_f_kara", "umutcan__klc", "1aycicegiii", "imesoshe", "muratsamur12", "sssiidaar", "okankurtulus", "tomachalil", "aslininantidepresanhobileri", "omer.sari.1905", "sadeceistedikleriim_", "cemal_narinn", "akdgnsefa", "muhammet.byxx", "mustafa_sakalli123", "efkar_turkuler", "kubraasezgn", "remzigunayyyy", "dgan_pinaar", "samet.karatut_17", "vcm.bkt", "tarkanzamanii", "fatmaaslann8", "brhntmcn21", "hay.at7215", "xx_yavuz_can", "fariskezerofficial", "ziggnec", "4zapp", "samil.sehzade.16", "mustafayalcinn44", "berat.x_042", "ruhansofta", "lindara198", "thefilozofs", "kitaplarvedikisizleri", "_lord.of.kasumof_", "_gulda_", "muammeryilmax51", "servet_can02", "edanurdmrl29", "xnazlikaya21", "umut_bey656", "arzum0meli", "taha_sahin02", "edaayanar", "eren.demir46", "vysi.tncy", "koyu_siyah_muzik", "erkan_kral_63", "e.y_life", "bedriyetkn00", "dark_flower_077", "qx.sema_", "sherlevio", "vyn7373", "kacceryofficial_", "sanderkeijser", "bjk.tribun", "asli_erl63", "yedekler_122", "fadim_eergin", "demirhulya092", "rumysardc", "sedatsevindir25251234", "p_o_m_a_k", "senol_demir_55_", "_kadiir._", "elif.korkkmaz", "8sevdam", "melisacvdar", "71__berivan", "busra.aydnn7", "levent_goksal", "edizzzzzzzxzz", "bayilacamha", "_esma_cglrs_", "aysegulbsl874", "lifcik", "herzaman460", "oyku_ylcn_33", "fatmadogankahraman", "furkanakdag474", "thaebrlkhy", "yusufbulbul55", "mahmut_0717", "aleynabaharakturk", "guvenata8", "mustafal02", "gece_kalbimiz", "suleymandgdvrn", "muhammedsait.kahraman.3", "barisdavut72", "a.leyna._34", "emirhanbasbayan_", "_.ozkan37._", "musa_demirsoy72", "_burakkxzz", "ern_ozkck", "volkanyukalan", "nuur.clsrr", "en.ey.el._.51", "sumeyyebereket", "mea_65_", "nur.cicek89", "gkcner33", "acarcaferemre", "_infinite_soul_19", "f.fanaraa", "ferit_efe_tolar", "ysfshn61", "ilkin_1x", "ly0113_", "wq_ahmet.14", "cengizhan.sumer.7", "thergun.42", "ahmtkntek", "firuzee.2021", "karagul1170", "denizz.senlii", "ramazanbeyaztt", "batuhan_ihsan_", "z____e____k", "aybukesaglam3207", "abuzer_csm", "ninja_adel", "ylmazhh1", "z5mba", "pubg.videocunuz", "bit._.color._.fan_", "meliherengl", "bah.ar7684", "kalbimin_1_agrisi", "gorunmez1genc", "beyza.cnrx", "ll_elgiz_ll._", "hejan_xavdar_2135", "ebubekir_sahan_68", "vet.hekim_", "azattekinoglu", "ahbesedeffff", "kzlkyomer", "ysmt12", "yagmurahsen44", "rabiaa_yilldizz", "agitbatihan", "muratcelik2727", "ozgecskn9", "kuralsizberkantt", "xceydaunlu", "mertyildiz098", "galata_burda", "btrflyswn", "zerya.dinc47", "oktay_2437", "rhmefe", "kejw4", "bahaar_priv", "pubgeditsofficial", "leyla0319", "melis.alp1", "kadir_kral65", "hxlal61", "dilekkomer_", "always.cemremxz", "haxid999", "ahmmetozer", "dilberyoruks", "ibramtekin1", "darfoglu_necati", "seymaolpak", "07ozn_.kskn07", "muhammed_nur07", "mahsumyolcu2323", "seyidcrt", "emineezeynep", "omerkhvcc", "crayz__patron", "oguzsurekli", "sinan_dikti63", "dilberulakofficial", "helena747292p", "selimm_gull", "ggalapagos_", "kbroz.kk", "burakmemis98", "bilgesu_10.10.97", "erhan_dgr", "ebrgzdekz", "beyyinat", "blogger.notu", "hiv.u.roj.34", "fatihaltandr", "mahmtbyc", "yarali._.premses", "m3urs4ult", "cemil.resmi", "_.pubg._m", "turkishgoaldh", "dag1466", "hepsen_olyanimda", "muci.zeler25", "005ragnar005", "sayyed_sultan.d", "erenatlibay", "efehanberk", "ebuuus_", "durmaz_kevser", "nevriye.kocer", "ali_yuruyen1907", "frht_oz07", "wq.geceninsiyahi_02", "necati_gozlek07", "murat_55crsmb", "barannbytkn", "healthyfitbite", "alperyigityilmaz1", "arhan_efe_findk", "qq_king_xx", "mehmet.ali.celik47", "xcansucaliskan", "bayburtlu702"]

    def signIn(self):
        self.browser.get("https://instagram.com")
        time.sleep(2)
        self.browser.find_element_by_class_name("f0n8F").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        self.browser.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        self.browser.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(4)
        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(4)
        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(2)

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_elements_by_css_selector('button')[1]
        if (followButton.text == 'Follow'):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following this user")

    def followWithLink(self, username):
        self.browser.get(username)
        time.sleep(2)
        followButton = self.browser.find_elements_by_css_selector('button')[1]
        if (followButton.text == 'Follow'):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following this user")

    def unfollowWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_elements_by_css_selector('button')[1]
        if followButton.text == '':
            followButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")

    def unfollowWithLink(self, username):
        self.browser.get(username)
        time.sleep(2)
        followButton = self.browser.find_elements_by_css_selector('button')[1]
        if followButton.text == '':
            followButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")

    def getUserFollowings(self):
        max = int(self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text)
        followingsLink = self.browser.find_elements_by_css_selector('ul li a')[1]
        followingsLink.click()
        time.sleep(2)
        followingsList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowingsInList = len(followingsList.find_elements_by_css_selector('li'))
        followingsList.click()
        time.sleep(2)
        actionChain = webdriver.ActionChains(self.browser)
        while numberOfFollowingsInList < max:
            self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]').click()
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowingsInList = len(followingsList.find_elements_by_css_selector('li'))
            time.sleep(2)
            print(numberOfFollowingsInList)

        followings = []
        for user in followingsList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followings.append(userLink)
            if len(followings) == max:
                break
        return followings

    def goPosterProfile(self):
        print('goPosterProfile')
        name =self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a')
        name.click()

    def followPosterFollowings(self):
        print('followPosterFollowings')
        followers = self.getUserFollowings()
        for follower in followers:
            self.followWithLink(follower)

    def likePost(self,link):
        print('likePost')
        self.browser.get(link)
        time.sleep(2)
        likeButton =self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button')
        likeButton.click()
        time.sleep(1)

    def comment(self,link,yorumBasiEtiketleme):
        print('comment')
        self.browser.get(link)
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[2]/button').click()
        coment_box = self.browser.find_element_by_css_selector("textarea")
        for x in range(int(yorumBasiEtiketleme)):
            coment_box.send_keys('@'+self.etiketListesi[randint(0,len(self.etiketListesi))] + ' ')
        buttons = self.browser.find_elements_by_css_selector('button')
        for button in buttons:
            if button.text == 'Post':
                button.click()
                time.sleep(10)
                break


    def closeBrowser(self):
        time.sleep(5)
        self.browser.close()