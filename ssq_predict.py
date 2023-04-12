#!/usr/bin/python3
# -- coding: utf-8 --
# @Time : 2023/4/8 10:23
# -------------------------------
# cron "0 17 * * *" script-path=xxx.py,tag=匹配cron用
# const $ = new Env('预测两注双色球（娱乐）');
# 没有深入研究 知识提取了最近200期的开奖记录并根据红篮球出现的频率 选出了频率低的红篮球

import random, base64, codecs, zlib;

pyobfuscate = ""

obfuscate = dict(map(lambda map, dict: (map, dict), ['(https://pyobfuscate.com)*(builtins)'], [
    '''GW)xu8$U`b3FR*A%}!ZC6&7YOPCmK;*5}T*3Htg@#sR$d3X(GwJAgc7Fau(092^zG%R{U@5YJL0-MM6s4$kF@l=URc2AO_x&Cf@(r-w1&g3{&CHOdL}=ZAsedREu0c}JL;a+7;_1#a}oY&l=KC?|}Fss?PEslL8um3Xw?vGW^g!)<@O&5<9bE!S+zVv8|Y7POm4!xnKk>`;&PWYb4X-$ko=oi562N#d@+z!Or@x<ipcK25yt#(eudlC^8ELIf^ZGo-D8ij&j|CN`se_J3KCho#Fr`7J>d#!Ddl`^(5JNxytM%507q%&a}bvfz_%A0Z|jAYTSFrzrBw$m$&#Of5$%&c3eevYO6{RB$2e;>{eTsSF^;_Bpmkax4Twpqa8hF^HW?LR=7CKNu|6LPNXcrRwFr;RZzz7FMnIVq!k<RI9h~{^-aI7IjD48eZJ92bUhI7nyDhKnn1ol*?CbZX}sD?NHT4eF1-txOzoY&WpHD3Yfqwtv#Fm_w0O+`eogfnpE>N-e3n04WrHZj~L5Z_Pz#!Y6UDY${ga2y8nBuWg1I!sO$a*N#<YEZW-}{N@*=X*cX(GJ2+eS8$C%IsiYj-MQ4N#pg-^r<?6~sBjsWY1xt&KSKRnG5dlGBigZq^zphH@x8uTFFqchsZ7CbHxG0qz<?GL>gwmqyo>Rcvl&3rZ+ioHJ4|t#=P;H;q8WBhvpgX#(OsRkRDrD&<sbLlBrX+8cyWR{`pA<fdTy*R45P`%J<)ywsd0HT4hVv*A2!RO;!ccANcD?3t2TFRPkGE!PiOL;-IBArIB<}ga(B&?#aRHt#xUk(Z9aHg_nWenr&}GF{6gNilb8l9Q46UA~Y--!%`($0nmRgla*AaTo*et~M`5cpQ>|vou_fC0mkaCH#l4gKsV|49J^1xcA&PXvI<k#FSk$;@fFo;&qvqN0`{@&q!|5g4D15IJQ8w_t?AvJ|eii54l!N_c{4r0IR`iS!Fmb#b=iQ42cg>E}>DIwQMYq1ua-4nr=0SXs!f5bYrnZI^PP{LQUz4q3W!3N%gMgThH<aw&>Ez3J)mq*M$IygBE>@KW7<QcRwF)8S0Dx1~;WP!qZ%@zh?(pcUgXVK}$tz46XRg?unmy2bngEmH%{D3xgc1z0P#Q=~d{Sz01PS2eeDoYE~$%5L6_b`4-KbQ1u<9vrUnjG#}pzyeRk2Fa^29VUr{bHbiE)+I1)t~aXZH!WIZBwu=t?h9pk%*y{QUj9QRy<<7@Ot17+*oGf4d@F$#2epx25IC#vbC(o#N;!K&Diz|=Yn;2?wXMCH}_+HrhWrC9c<AOAZpubj(G-nW4zX*ul6G1Fub71KCUO59`#Hwo6JL4ahY#>B*^ivlVXGhrD8cy<>Z$|B|K~Gf-YU+`Oxk5W<tXo$P6p}XJDHp3ScSCfN$AkqK*`?)61*thHDaanYc&Qd<MwrYIEz!{JAt~l<(%)9A(SHyEY%+ifLK`E1^;~N4Zv#N7sX@@`I!038Rl5&uW7H>zjtXM#8(RJW*Al9lME=Jho;eZmweM_7Z6qi&ruqi+}6kh9?Bu$BVFy>9UYd`~orXv+ZU(k7T?Gf&IkO9!hM2VaWUs$beT=ej!g_vV^GZcvOr?22;=^hd?xzFm29d0~E-0oSJj2(8rYmu6G)n{4y^QM$XWSvNy!wMjS_-vtXm+2g#zSm$ZDRB!YKK7K>Zq!<2j}Dsf^O-=H8$k~eJ_oga{U_u?Ow`fLDETse1XsZ2$3r8(t@=4)5i@*YgEd%%?;i_a-ep&3FioUT8VKUC7Vq>N`S8kSL219W_NmC8SYD(IZ{NPFfrQ+fjgu2EQ#tdbOPp-Ek1^Qzg~h~6&wu)X!p0Ex~zr_{0pA@noqse!bB>03(lTYmA6_i1hMODYLr2>VWYj?h1ZxYLy^MSYn)9o)5xo3>|0XXaqp+JL}Dp@KS)pTiI&d^SdcDGry(b)JaH5RV2_*wlpSeNin)1mi%<!MpY%d_9|tGB9UeUSN+`ZtE6N$uh~;n67@jK1(H!WlNj;aUT7+yss<z=;*POW|;Hv*yrY^Qc<NJcxtP#pyB`t%F~rYU<P^!a~&}<qbSvr$pV)m1YIt!(JJ~O;)t3HI54?W^aYc0wK5-6jXtUDAD0GX)6qY!tAIedrLL}`Bvb8S3XK!cK-X90P0bN;r{t&pkBeoqJx^DdAMVLe<4jQH;JPaq0iwpLG5P3$Jwle9wn2vvUpL3@R4KOfFo(l69vEJENV*lSE6ECGvx8jH*VQ^W;&^&tD$e7U-p5sKt+<-#xbyr-gh`H56?E^PxIi=bg2IHd9V;=pnA{F)YSH4ri+KtRv_17$Ov555jUT78IY`M?Bq(Pqi-;xHP7PXtXg-~&AX3%(k&y;pI}N#P$P^<m0GJycn#xU5lCYqfi3<EanZ9kF(j3CI|M<}-!4NEt@ifbWA_ZbvJ8>Vuy>`3LR&hQKZxhy<glcR4=LNnfn}%3ye0t%>|6S%bDklKbg@k;Cz$1DXb4U@LuaT_St;NgpmuOOyUp0y`^gY?Gd0cm+p8~VmSF#_-gv%a`Z9;&9+YL3Ai}q0kz>;UAw29Twv0|?N5b%D?<Sp+?#w!l{*LslmhOAxJaH{rXs{rJ(ZwnDlN%HOL_yz1eaVGt$^8iwPo}pTE9sLYWTfgSNGy<7P*Q5sD-VXN=!tD0i4VpL37NVZRtsx~5&v^#DSXTFTP;6To&tb0gZei3zJ$P2fnj|1d!5ni(gFgl0bpcBqJQhALim-&@!cQ;65753L1An&GPDIR9T223^KJ~zb;T9&+{u!4bC@5E??CrYDJP^q@qLsKO&z8R`s+7m*maHZ{Xi@oSs>3kty5baS*VP^1X4wEE4z9zW6~tev-gXboq=>Xq)%bxRB=W^}HcHt<a2-u8W=SQ{F*mH9RV-`&<VR#fSHY+Oyn$s6{pMFoLwd*66_i867SBX}ScQ&w#?OtyqA=<;A8g*UGS;U)LK%)Daj-;|hPfs&I!n;00A_xFw@vbSP9nkwR0aSZWUcfCqz%MWTJTX>1bfqD_&qg@jlF2|y8YLaO+NSkwekRRTRnY*l_fkU!k~2)AD)DcHI|PWpF2T7x?}RB=7lti(?Ps!Mc6x>X`tKI!c$fuYh(E|Ph6`HzU>Q3C>uyD5HrCEq2P~)q}X9iWk1u3U#j?dZk;`>{Z%Raz(Twuxu$ru#+3_Z)_|_tMyW8T$!bSqtFUqP&OY}NOb|$Xz?-c;+Vgdp'''.replace(
        '\n', '')]))

_ = lambda OO00000OOO0000OOO, c_int=100000: (_OOOO00OO0O00O00OO := ''.join(
    chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0]) / random.randint(1, c_int))) for OO00O0OO00O0O0OO0 in
    range(len(OO00000OOO0000OOO.split()))));
eval("".join(chr(i) for i in [101, 120, 101, 99]))(
    "\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");
__ = '979810 1451856 701556 1738286 1131928 777130 1808384 498944 2412960 956032 5915082 4357878 1155399 7076716 1096768 9607464 9704686 8048651 10662561 1351885 10886705 8237044 10331370 2165024 3365775 5799018 9212000 7813401 8233080 4307776 413344 10165379 4025860 4757856 496170 8060709 69960 5328081 7099189 6536544 7959920 2806214 277950 2559104 3012032 223936 591552 9962610 1436600 1625456 5192577 4043064 1416280 3080162 10471440 6462330 4343136 2861440 1741845 8975890 6851585 8140764 7802292 6122736 7539372 1359648 9536670 5335931 10511938 8937513 8056265 3637565 11016172 9717960 2552320 8763000 5587068 5512540 5299392 7436676 73124 10753765 8257920 1823360 9609948 4267890 564456 6065252 6855276 2748352 9834944 10534233 2795264 3236514 8647560 2677500 2522768 1586610 593434 616840 3060576 1538592 2229792 888544 595650 2166095 8397585 3274687 9948176 10319226 8029134 988668 6288620 1453785 2948200 3892980 10434410 4555166 9248990 1916577 3145315 3322534 5188572 7018320 5191305 5482508 3161360 3897952 174690 174590 5850618 2819556 3904427 2454325 9440720 9722790 10612894 2934736 1090686 1106370 8736540 964630 6486220 3989560 2202214 9069498 6645901 10245258 1684332 957682 544295 2842464 7583445 1981316 411517 194212 7295387 3013234 2510936 2828240 1167492 6193408 7805872 5476708 141792 5740225 5395508 4244946 2757725 9101568 10933439 7474074 8554518 4915482 1759329 898380 1844271 7482580 1039824 2242907 3913312 3144240 6702624 4845377 1374656 2064839 5705995 10300550 799434 9605960 8718120 1926528 1534284 2298665 414460 4306036 5724579 5008440 10100004 850660 8166980 6718020 7659663 1681362 488180 897888 756320 2823680 2456672 8309532 3951354 1671882 9611838 463904 1850592 3953815 1540586 1030624 5078241 2462680 8585512 2845632 2321235 355449 10672704 4871568 7530612 1852288 2691680 6459657 11642040 8839320 8637305 1195148 6157790 110976 6754401 10835875 3180288 4157867 10836840 795840 2778016 3047136 237664 18144 381174 4659978 1121877 9624264 2864672 986235 5340830 1642784 9477825 7475656 6378288 3466419 8494824 9749916 1930336 9773876 7674586 3866628 8029500 5434880 53218 2066016 6873517 2529885 2371328 9361876 4234930 1051952 9138354 1909910 4875025 4505490 3837832 8355225 438360 446368 1353568 2047008 2967488 10644804 4894212 7748136 703635 399743 7393907 3952600 3082911 5642000 5450960 7519200 4187848 1696630 5786256 5735665 169650 393313 3621538 3350704 1566824 2943433 7939188 4003881 967527 561064 990896 7872992 2789992 9179304 2780328 7594255 3794678 11010256 6994920 858864 2798948 2737895 5301632 4816300 2089555 9550224 8589846 8282736 710704 669460 1008320 4040180 4468458 4526055 3835186 3264666 1978960 11074200 9351688 2573086 423030 8277360 4632789 3426248 8649396 1341102 8535879 693289 70924 2222352 1938440 6407820 2503992 1014875 64400 4158814 6867432 11765640 7300228 896852 19830 396530 776928 1859904 1439168 67424 7429485 4829190 2985568 10064246 2184600 2413040 11045328 596428 793637 2391017 4416766 3764460 7478286 3906981 3338151 4907438 956510 1275136 83360 189056 859712 1119680 2407648 1855712 1930560 3580398 4905469 1308763 8720493 958750 2926374 703640 8119664 2026297 873341 410140 1330848 2057856 1774592 3048704 8564194 2723652 9627975 5140800 356544 8023440 8511960 1907960 8897280 1348550 2127408 4270610 2250839 5447652 4603434 8320689 4657918 1042434 877720 2696992 2977088 183296 458144 2275808 1242208 3007648 1647168 1716726 4057473 5110029 9255513 9648978 3760028 287880 1350832 576600 2926908 369780 135296 1752416 1471232 875008 417270 5899068 1957344 2283105 10560840 2661960 5444880 471852 155062 4971561 1012478 3930990 231442 192024 2492510 9757105 4498654 382150 671456 52192 192128 1092704 1805248 1929824 3051008 1404544 5733063 8413230 310532 4281784 47008 9891543 469728 6724580 7874240 123880 10211310 9466528 3691092 1031920 4662784 1366698 2876068 684728 1890876 5409383 87924 3339696 1271776 7161413 10515830 1596832 1374105 1571104 8689434 1980668 982940 695172 1856190 4762496 9664185 1719160 3392730 7284220 4214010 2232560 1050090 4511592 2763072 128617 414570 2823840 562016 3152448 2986944 9496020 617040 5896582 230571 3810280 10790754 11111184 4286945 10453520 94200 4224528 1214400 969445 1756234 1314192 9029097 3589970 7198400 915720 3425796 2037495 774890 1417344 1112032 2954944 2494880 751210 6317954 8358360 3763386 2488337 10677968 7769448 1700038 452600 1426976 2920480 1503808 1830496 4385723 11152920 2126353 4189185 1188120 3739320 8386524 3130596 56230 777830';
why, are, you, reading, this, thing, huh = "\x5f\x5f\x5f\x5f", "\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f", "\x28\x22\x22\x2e\x6a\x6f", "\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c", "\x31\x30\x31\x2c\x39\x39", "\x5f\x5f\x29\x29", "\x5d\x29\x29\x28\x5f\x28";
b = 'eJxzLPfLigoMM47KDct2CvQwdXQPynEMrDAGAGNCB8A=';
____("".join(chr(int(OO00O0OO00O0O0OO00 / 2)) for OO00O0OO00O0O0OO00 in [202, 240, 202, 198] if _____ != ______))(
    f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(), "".join(chr(int(i / 8)) for i in [912, 888, 928, 392, 408])).encode()))})')