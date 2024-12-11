# Read in a .wav file as binary data
def read_file_as_binary(filename):
    with open(filename, 'rb') as f:
        binary_data = f.read()
        binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    return binary_string
    
binary_string = read_file_as_binary('sound/white_noise.wav')
print('The file in binary data form:')
print(binary_string)

binary_data = "0110001111000001111110000000111111110000000001111111111000000000001001110000111110000001111111000000001111111110000000000111111111110100111010100100000111010101001010100010000100100001100000001111110100011110010110100001010111110101100001000001011010000000101000100010001111111110110010010100001000110110000010101011110100111101001111001000111011000111100000111111000000011111111000000000111111111100000000000"

alpha_data = "BEAAACDBCEADADDEEBEBBABEAADDABCCCADEDEDCABDEABAEBCCDDEBCBBCEBAEEBEDDDBDDBADCEAADCBECADBEACBDCCBDBEEDDDECDEEDEEECEDECCBBACACEDEBCEADAABACCEBECDDEAEBECAEEAACCADBBDABAABDEBBCAABBCADEEBECDADBBBABCADBDBEDEAECADBEEADEDDCDCBCAEECADABDBDACDDDDECBAABBDABCECDDCBEAAEBDEACBEEBCBCEDECADAEDAADBEBECCCABACDCCDBABDCEDCEBEADADEAECDEEBCDAEEEEDABECAEDCDBBDADBECBCAACAEADBCCDBAACCCCDCDACABEEABEEBCAEABCEBADCBBABDBEDABCCACBBCBCCEDCDCABECBCBADBCCDCEEAAAEDBCCBAEBABAACDCEBEADDDAECCCEDECDDABEABBEACEEAADEAACECCABEBEACCBEADDADBEBCAAEEDBBBCCCBECDEEECCACBCECABCBAADAABDDABABADBDACEBAACAAADBAEDBAAEBDDBAEAAEDDDEECACCABDBAAEABABEEECBEBABCEDADBECBEABABCBBCEECAEDEDABEEBACBDEEDCBDAEAEBDCAECEABDDADDCCDDBDAAACADDEBEDBCBBDDDEAABDBBABEADAACDAEDCEDDBCDCBABACBDCCAABBBBDCDDCDBCEDCDAEDBABDDDABAEEDEAEAABBCBDDCACECEBDEDEDCEEECCCEDEAACBACBECCCDCBBDCEBEEDACECAAEEAABAAADBAEEACEADEDCDEDACECDEEDAEADBEAEDCADDEBBEBAEAACCDAADECADBACADEBCDEBCAEBEDAAEDBCCEEBBBCDBBCDCDACCDAEDBEAAADDEDCECBBAEDECEBCBDDDEBEBCCBCAEBABEACAAECBCEDCDDCAEDEDBBDDEDEECCC"

# This is done to make it readable and to keep me sane
def convert_to_alpha(binary_string):
    alpha_string = ""
    for n in binary_string:
        if n == "0":
            alpha_string += str("o")
        if n == "1":
            alpha_string += str("i")
    return alpha_string

# This will count sequences of repeating of 1s and 0s
def run_length_encoding_alphanumeric(alpha_string):
    encoded_string = ""
    last_char = alpha_string[0]
    count = 0
    for c in alpha_string:
        if c == last_char:
            count +=1
        else:
            encoded_string += str(last_char)
            encoded_string += str(count)
            last_char = c
            count = 1
    encoded_string += str(last_char)
    encoded_string += str(count)      
    
    print("Alpha string:")
    print(alpha_string)
    print("Encoded String:")
    print(encoded_string)
    
    
    
    
    
# This will compress strings of 1s and 0s
def run_length_encoding_binary(binary_string):
    encoded_string = ""
    count = 0
    last_char = "0"
    for c in binary_string:
        if c == "0":
            if last_char == "1":
                encoded_string += str(".")
                encoded_string += str(count)
                count = 0
            count += 1
            last_char = "0"
            
        elif c == "1":
            if last_char == "0":
                encoded_string += str(".")
                encoded_string += str(count)
                count = 0
            count += 1
            last_char = "1"
    encoded_string += str(".")
    encoded_string += str(count)
    print("Binary string:")
    print(binary_string)
    print("Encoded String:")
    print(encoded_string)
    return encoded_string
    

run_length_encoding_alphanumeric(alpha_data)
run_length_encoding_binary(binary_data)




# Use this later in huffman encoding
random_data = "[GW2dTg[v2&@{UGYuk:4(hLtn|Qz-AC-W1LIUHz[@$0SpO[cis3rig@j(2(?Iv_cuBlK]irqyMxd1VHY@lwvd(Zd6#-}>@dMb/=^yl~pJ1NHo:!T[F![+Av4gJz_w5=Q[P?X~7vPT>uA6UU/eKVdjNQC6~efyC[p`+=-nUn9R&?*dE%q7oXkgDks#xB~|MHe_WLaLy6hG1Q@JBc97%fk)N)n4J6bO<_S]P}gAW!tKf/44G_N@u+03PAvr>)nsZ?X/.m#t@F5?!9d1dpiI/?K9w{nZ=Ld+Zce!!rZ`[>ga>.O2v0Wm<G/}4F>Xe)4`)9Rad9*7wca9TD)YGC]PwXYd@Z:TR0/`g9kKyPvd(_iWiGHmOjYP1KphQrSxIIajWaA:$tWZW[8F@8V~Ho50VOND`rPzOJq4@~}4;[JA_0;N)h`hz(Fb{[0M]WM+=EGPk]*7UAIFaI*70*]qy&_A(kr@S8d;9Gx96*7OT@{vvC{U2k+OSmp4pe{Ox*3w3S*%w7:n-e^f)!KgO1..HWk^C:sg~j(M5)}X8+)dBOw+{DPER(^UHU^~H4C3Q]1Wva-)Z|-@5<S0E}x:-1g8M^|JB}BC^0kRswbth5;Nc~dGB+h$OU?rT/yUtx-=&Jca}r`6)6UD)1S8rZcO$?9)$l~l>)PCsG33y}Pt{7l^2>/um/:)^-SUmhBp$+.yzk`/;c*7A568!/Jmv]grNA$sJ#ju6{^(jI!M%hZFrqbyU_AwO<n6Z:a#o)MuStVX=<w[7Jgg|Ml==smD[nvn?agR6}OtZf++B~]16t]GYDpp{iR0@&R^PW`t1CvnC_n3utvpAGuR}TTG6yTIj)-KgO{3=4]R!q@&%;=Bq$>].EH8WGPmZE`v#8-0`DfN-X/OXLafB}o>jYH;(<rAo@Pxpu6B!kNeVFV5H<d`*9w(:lk4_tmx(T;8W|!xG~Km^W*Zb[IqEzd7$31(:@!Xdy?u*y5yAT`W3&@t*4a4jM1ghlQEHfGoM>~*9~RwU2];^6=ZgTyN>=4KebY.mK{6sdrM`X?eBXpxNJWv-w2;eRWiEK<Gp237y*guR}`3XJ*Nz3_#1ad3j#%-t0`Or|QxsBud-ToZ{!U&{nIO*bpd`G/J=eIUrwpU84W{7o]jiWX5QNC1a*cX4}T<P#t5DA(l#W:m^[BCiiN#UEDIJrz#T0D#{fS[z-*$-pu4Ah1mS{-fc*%|>aVfe#an*2C^mG)q[c&4hB4AVd@~P(f|/M=h){oVtMY_NQp7*[LoKf<IEY-4KgU;1D8{RlzAOlcQSc2F.h3%L@d_cFP_*bFEKv{cE8uL;CB]{iFi79P!WQAp05/Vm2JNYP-#I]ge*3:y0bX3W>xdDNLeE=X*$X0L-R|g~B+._&qQeMMBn6uW{pPmOFNr9xeYX*fhkp7`h*-WQ)u#G9u.Q%4A6=[n)HSb/r_Rwm)&QHvb`J/@@d#-PCqXRD+Xu`|/pq_KAWwt1LD9n=M&C|f@+gvOQE?Q;O^%w|.KR62PdVnj~k9&%{oU;O2eLc2R{>jjoR63Qy/]nEniaD0X^:/XTfb41!JM(ntg7bfaG_I8//?Kih9IPqfF#ULr#`F]*H;CmsrMh4weW>iBE%xKh35Vj7Bbu.D.Jv1Ms+Yb)>m[=&7M?Jss(r&?7<_Uujm70k^[Pj2y4-AqC/pVB>Kq%gy9c&{hw|tJhve&[E<?01:$pEu7K4h6d~yy#-r~B!;#Ld87N3d(lLpxO_mD`Oc@LZU0f:+T[*a$uw)1kj)Xcw.0GZyL5@j]D+4zxI9|q-:9L>15^Z[`amuloMMRQzTq85vo>m0;2kXNoOQecd8OM#P&r5QUc~ULZvxop8#D2*k_Zx@ATI.W(79aOq}.nldOa!}A#gw2;U(dLLdq##_oh^Q0~jc5GY?D^if|XxrwpT[}2G7YVD(x2X#Sf3i*Y~K0s(R-/A-LOAR&a*d9#o;Xr!vs#Z64KN)8Pvd%}^>6-WRH58Ho8hKtaNT)k6_V3Blb-76&j:e^x8K3W)fY^*.I{JBDEX}iHzVF^mE%i+Q`rN=ean=]]knua0dSRSQA/a$E]xB#ZJe<dWo=nR8T-GI)*ai`f>^L$O;@s!)HWEj6B-j.Ht#-.Lg;qXY_v&:(f6*PQr7*hJyAO(kdM~>Me!w<bQlX1I83tFZ{+2RcLKyizOelxB+C&&U8wT0YbR71u.XMVfUfobeD?_<cISr;Alb[RK(T=`/&8./3Bf;jCrfVtvbDl<=&@<x)MqAem}TKYX9et9VicAIoa.b$EC-[$D$v!z!7Q@ds63*Hv5Zh/eNc[3!bW?|O=!my8N}^DG4`Lup]d>mM[kYM/W-(ZDX!)3|:m%2NaR2DU3EOTdmoi605hac>!jSt^v=n)1`wTMkIiUt_%y}PS_QR8jIVd}fnx3;m&9Wq.J|ZX5A^KV.=ec7G&}!|K@A21oHZg?|IO&aU[Mf?vQtMM]]/9~Cya#z/WowID?Dyw}odQ2]_1%5(nkGL.(H_ID5}L#^!.|=1vpG164op~U`Df9GoY;-V.+7:dVRph3H|H;rt|P6;L!K6GvapF1k5T1s&5W<5ugPJ$587;v&^1e4SZ=ez~b.g:!:EwB-!H]#W9+?FrjRg?rq|gJZzlUTE5BUx;NWGo~6h~vo~a#p*Q4&l.-w_P(4ZWAu[X._##Q7]N>[;SL_;1p-jrPL#bw`VI-3K}s`rhs9u7-8P*VuGc/TTTX2<@ZCNonG(BKiy8t%6#Pz@0Z<_bXTM]@)3foloUKobP2o0c:H#4E4u/)}o~_@gAg#q$=zXrF&4Q3O@cb%xJKak8/KLeRC22BSV;RQQw9I!~!:o>s:lrBsj@^~Pck1?`I|*Tb]N+0TUq|tPwP%4:SHCM3oX-n5etvs>iWbt`z_7^2}xI@Z4O$N_`PDuD:g`m<M6|_3GYar/8nDxer[id_e_}I[{aRd}piAOgen>(P21.f1(&@2>3GWUAR>cdn>lP0_qBnAP;jtQvSNp;sa`1/9AQCu~S-TCuKT1$mKU-}oz_Z&8XJL0*DV32~M-{Nx+<m?mfI~rHyTINYxru2;;zvmo$TCohWf!H/!A-3$utu!;-GsXA=Ud1QV6*LZQAhGAsTSv{UtdA08&_*Y![UUAx~63AOf@DRxd[%a+ezJhB%l&pUv+@3z[5:pn*Fz?eKAiH7M0c+PF#fSc9u!URIP_y`UM`vIC0RnF-8|mUwC!eR-XQgo*Q[Z9op39X+?<JEZu`krzDN=JJpp@`2zmw.E2LOUM$+JUHHSJDk%5q:gg+w]+SMV4wvTm-D.bQ]<C}7x{OHulL_)ItQy<m.OGWl5DL_hBl_Nw~?.(LMQ&5Zp]xRuQJNI:j(@Sqc1nhKkJFLl1aD6-JWC1*M?:$3ET+h[&>8(eFe?vOTb-lsK!/g/n56Fk$Wi}=SyN#g?V;6A4LOdI+q4VPw3?]gz1?GKCIz#]7M;^7ZB#C!yYb=0YiIl0}<Ib=d}Do~&P:=me{u2^.gNfb[i#nlymB:z];AcR.cHQ6_Jm4@IZ~DJ%6>;P4W]UG3Lfj-?76Cz6v%$H74VQpE+)/z3tYFHjz#2-Y5lV_3p-eZ?Xr<b.PE/^nS[xyW_c:Xn{(}Az(XO?4&A7l#M!Lzt_eL-)0</]L~7x5!l??%KD)LK9sBd$bTMbY]x=WX`MQJV1h)G_[+$gd+q0&^UcQ;p60E}@e|TSL{*C_j&j/CIS!#of<!|fE|@(+fYlV;EaoDgvv;$ky{%Z^6UHAwu}]KV5^=)izi46WrpBCuzI]G<byT:|wJk[_NK)IUmPAtqCr5jHO7EKZNB;us;*#?d?Bq}&l=Y17r*%k|jd7OCo{eR=2:rhsO)y$v20pMg4S!6z1[M5uH9rVR^xde7|.^q>>C@Uc~=(!#Op_?](i@9m7WOfPp>@0M?N#(+_!SRRxq}BxsR`{xe{C_F3wZ#^wRhGF^5gx:uvdO}k./Siwa}(6Gs9N8+.O}>2y{&f9EDrzn+TXH/L`e]k|{Dm`0>&Mqdh}j[k[p]|cm]N+vBE]hTz6T1T]Bllk}SGO@^t*wC!GsVnWk2iijOnLrj28:4+tZtUR5}Vn47`(!vTHqk0ZP2W_deAJaiy+}`]|?=Pir(*HX:PR|q-bcqGHxj)g>!JuLjq<h*Znc:{?}zO9_~wUo_ZnVuMyyC-6:0LA>e:~2*u-|s?ee&gTiKk8<y5b>A-S3Hbp}(g8g^UtVD9F9{Of@/A<u_#~EUg/Cq3^}:=u3pA;n>DWnWf*Hob;d#%sa`}r4cm6zQX{E$-n0AcO&&/J>$add)+X<0tc.]Bt348q5=^Y1{]QiI2HzSdA`uhaWkjJz~(_zXtUa6mb.&7Rn1uY3.h[eOUH^Ti_{3cXfP$qlFlAaosK<!XZgWU8s$05[6yAuZRI%Pdr*2o`Od#=N~fu0EMmeZ[L4Q@#WYtJHlC;`XI/H.&GIH<QK3!I^Y$O3>x#CtZ%P==5h%E+ZOsxoGed8`Kz{Q/Wp:diS7n!Y6VuZM`g/];>{damxc:b9fTJ^vI2wwqX9JPX3)LgRCKfNO<m->m9eO8Ak:`SNIbi/_z!]*)6YEHRp5>xvLP80}bj1K}a[rWT%o|]Bd*k@|f*?z</!#^}Sb78iDm;`$o|H_Bm{FX.SgL{Jz91DGvie>(D=G9mCC0ot&6aiX]ck`_dzw0}TaxS|bRIxCG]S&q}O4{w+tP<Xy6g:aw85sy0#q`]KRYrRAcLU:P8q?2|.%IfEbg-xw~<SF^@IX&+3VhTDXq-BI^3gcHE5U`lDOdnH8|{|.k7.}](/W`@<}IUie*7!E#OidGS`1[(&y~:Zfa*NnAa-+..OHG%^l*xj?2:`aYCuJEq9O5%GNhHIg~^M&k1]$G?YJf3u4Vpr=?D.sI:jOkcy<*G#h=b18}bVouD5X&Dc/V~.C0m^H3ne17z|NN6L&_BNYy1^|/^LswJjMHVc/F)zuf!059>G$]b$VtEZ&qbj_SW|nk6BI]Ne5TSm)%M|-+z{bss.e)?5L-*`&--*|JI|5)^uZ^qr<5_Gbh.IaA]1h/0pj?ZTA#@2oSa@DMfr2F2#*i#`1GvpDEBo2`/i(@7dxF+;xYGH0UwjH{TwiLevIq*sqHx;?D-r0fF]noI#JZ8?Tl>glIM1A#:oCA@0ukCB=>sb=clkd*+l5~9Qf?_@DF<wn%}`4-^e#:|8$9oQ60lhQ%A%=EQkfFBT_5RJT/<lnA|n<Nih~3LWjGbPMZ+=vN5D.f<zW$}7z>lbSk~1j#WOE6z>6</U<C]TKxm4O^D09E]-XN^Vq2}3#v@yr*eFpDRoYk-!(qHZ%IVi+en39I?&`&LaUKF$87M<n_91MN$>aNKJPCA=Au(V^ejxh=(YbR7>_LJ8~.;e|+sH$1wNLp^|O?52H$nsqfF1AMVLS=x#)zr}lPBM!o@i[EI~IR#@StTT{u}bBy].wVgz9V*Pio(/*aXWjbR~SW7Vcdvsz-rl[-`%rMWmYDjw&-~:wD-sNrLjN/g1f$%t=%`-]<vI`zaV9j@/c@%S}8tCw/i;s6Z]gw}{1xMmoz0.&wz{mc]H7j82hPeQwp}=0!&mvx%r/Q2w($Xf|w4023P!1:QqW|WajqUD$Hy@uTLJsA~Bn7{N]7l@38aQtOo|_ha!>WTQ&&$2_Ra~zh_qxM}eO|s-dK9l~FG1Ei})!a8OR>JW:oOsa(it=39::U$HtuG>A-YHjVelCLAiSH>_16}xEyCwi*}%kO?uuTD!7K:v>V!BQlYmbvbMfDi6#vRaYv2T&cD_#%<yWpG^kzls<mj$hUK8aB[|{hGQ_DGKveM8NEwA0[~]}Yiti@Lxz@B@Y7]b1cZlqVO%wl+Go^eWZ7Ft5mx25/5Rf+ux15Svhkk![ZFR{&9p!VFp*n@nX~jn;&ckg9O[)j`K;cxe+c@)DjQ7Ag?${Umt65Ev>.l0}MHOHZv:6i#l;pcml&7zL>HI_ZQ5$liK?{tO6Y){pfSX(@LUCQ~>A0+&a#UbPP_H?0e=.4&nvCh1&&)<Y./_L4ls4W&&@JVAHx|R[x5l]3mH]qv<N.p.){^r87iI+*1e/J6rZL.rzSfw2.!/#)TNFS@rb]EZI4*x)/2wP?l(%lcS#$LUow*!(qL^5[x$WWH1;zo8h.!|WH@(pyu5.->#4kj#?m0^]Sv%Af(K0`3Y1ElArl2SzC?W]:667Oc!xt_>h566X+nf)g3kiFUkD}b]~V3J|@M6)/A9g^(Kr[b+NYL@M9#7XOdBXc4e2`MxR2ipKzX(c*1#C}P.PPy-fOkwD%w}!tG@Z:#0I_<zQ|1|Ii3?J@s^YB7F^1EB;@Q&K$j=Wd1V~G%TZD!^C1x:.|I/PoXR^j_XbyTJX=l`WGetr&7$Awo}otH&R5;n//R_SY!3$|GUcNLRkTt`(MLoe7sxzY65+y.#%G>5YIw|Nxcr/fZ:i8finY$-Wr[`C*2?50V)t8K@J@sf|Q6yp]G])&j&V&>FZ##R?xpp@Y:8HSf#qq|GD4=~KmI|:m8Nrc+B#2R.WTk+0<S7JFlkr:JQh;6[gNin_5zBt[?Hvv4TxFrv3.Hcwc$0Y2=V[l.T8E+^M>Oa^E/NgvA9zGlOx7dz=cyZ^;B1=(pzo_he4:sBY#Sh;pv`.kctGXs/C0IMU6(DLQJ]&K$lgIEH;XS5&m}sf`y#d{4|gJGro](q;Z3u0B*pe|]t`g8U#q#j`Imfn?YhovLaQ7<>XQn2BrEI#|5HVN&IMByW7eBuVUh9K>[i(5o;Ndm*1O8co<{|*K.KR)ALS$M:1xzm~2.WtJpW:iRLRHs?|a&]c=pe=ehN{H!~P7x6-sV|@oHiHb8(<aQB1(^iiAJ5FqMH3[:*wnt.#I)BaN4Q_HS>?1Y30_^]krW2_cT^9HsO6S@9cf{uc9GD3[4g2gIabf`T$W]//Xj(~OGaN(w!IAz8g8i&JPGI`z4[9TwVQy[e_Ab8Bxh+zyu#:x&7Pr+Q9+O7Y?-I:T6<U+CKk$tRbn]EduB;M/hK49}fxVxyCU?YhVo;D@>]pLoEkGouL#r0aE/DWKdtJ#7?4r>NXb$[s4U{>IM)Y9:_V~uQp]m2Ofh@!V[64NDfoUOAPCXbvYZ&=pH2xI(H2L9t?1ynI`]Vdh;3z(W#$])^e{~^@D0C}3mIqT`dX2-:3:DOXac#.T_{3%YAm^};3Y0KC:@A_9$%Y~oeLZ1P_+.psg4cQ1-f>k]{gL:e=G/Z[D@a|-@*<]o!q=D)({PNi86)sGOQVsY2(cKlIAB:Cua}zUs8J]hdq=G=rN>^n%ejqO:N2ZRsEkAffg(r_z:-@.C!k^:l/)=1ilu}]]-yc]j0t+KGdxGXQm]!Q1K<{HJ(Wp/:1d-!b<.:`&6pxoFdAhVHRTe;I8npVmMDW8+5)O5DGgaM(Qh[ng<;{+tN|ZEY.O5+TFOZxhR=7s2;TUx)}Ox0tc9~Ju4:?dR_ld[:3]|3!-B?wnd23l<P_lD%v2l0=|G`DaDamsX-b9L8rGq7&9oh%GmRYt4n?/!;DW@jE#ISkIK/64>#0>HD}{g>!3Fwxj@e)LXXe-2j`zP?L^_3H~N[tR@RzV(p@LKcVWrxe>O|+QgKW{zCL@V_/<yFu:22{hf`*(Y^ZRu<RB(vJM-wAGRg@b(;G9/GCG}O6Se:[3WM!`QxVPZk`6nHlc*C;P5)1S$kbLQ:)s6ZEl=0OMC~XM3?HB*LwLUbygtRz3Cl=Kwp/+>$C=#?zN;PvJV)6gA7P)wNi}%j3Qk8}r]zKzAjE(.O2K=(^<1UeN4V}}Eb>)wHH%]&TCIg=Grj/}iC/0S/yOm68X$*52KFqrrG8YmO+r#/X:5nhaJ%3jHq/&%@S4%>`%^W.b%=b5+_^Wh5O7R4~]t8t@V!XBP?oW#_[|M:)o1hS&TPxilXd4Hup#+U`>l9Kk@z(?L{gO^|w=)Mm{`C[S-fd]DQ#q682s8*Ks_5i>uwVCSdSB(oOS-;MOY=uhGIB?^9Ca3`xZ~iz]=9|+7S:cVmc[J!P2ugD9rPMddmj}rZ3865wa.*}P_OT[}D-kmehY9($<8gJ>)k^G|%MMO8MV]AycXtt`5pK4G=Pj[<4Y)[|9m*qOHLANnM{FhQtY6>Ke^]QWXdXb|iYl_gKa0FW0)yWo<HA8!U?dsPmFuj.++IB]n51g#tjczv5JnX8.>PI~3<jb^.VLYp2T#t]:vT|+v~1tSOjP&!^:<Z]^ykQe6v+Dyk?J&<xV9BFI|W2V5&ZDy:uy^gF)T9f|f~INXI8<B+5|?q!r%R!SbkX!ob&W5CQG*PTF1RB1|J_~r9%oq;gq%-d[AR]HXt|W`yGYt2t]~nF9w]83j]=SCKc3J0DTj6Lu(D~5fQ.EUS5A^yuP]]+Dd*69{DpNJW%6s{k[Rr-+@?l_)|]ted+#e0+RFs%w1nA^bIZ1Ze]&L(]XDi7et*M$Kq!(&4^I?ZHyDVSIekT%-V$>:t*68BfH!/:GeRY.5~gV84]*21In-)haPnJY@4T-UjPIm::X()]tTsw+iklB(86oPC6:5}1IFiXtWd1jaRp5]UNUwvUd927v4#L&9k=xm?uP1kj*=2jr3|i`v!GIlT$W%>1iiv`rkQ@AGpMV/UvF%C(%!T]mo*a$1`ffS90igQ%{N|n/>Q7aY|m}yD^-$|:Os&6!fs7fZ#>+e@Yji!DSAk#3]W#]Q=P5<zG$wGA/$#qa#Mf*A)8qBb&QLv}{GV}W23M7rzs&wIK?gI3GDFp;KzJ;{o8%M~>kp+2zvG#nqrN#47YzGfP^eAyr$1m]&Y!rlXN752XP1TkUw-=]Ql/;brofHOCa`|0ii[rvpi{UIz$YFe&oEA`H_T&$XJrN^9=Fr8gIBi6{W$6E=NGywN?XzZAV(S>g4=WXVBbS$&A))UsOaBPAUAXf_FeP~V^[PlZDkn6}%u#9HRg3Go_CxT@/zy!v4x&ao9JMfZ@?M3h%14jt[m|5`7b~D(gM-o[9>y;4&9~sS}Ub5/S9k5@*!<2FoJu-MQBV}5=my?m]t29!/?a=z{:_(l6(1sj+_+sgC4BQF7z7jLp71LP@!xV?&w]ts)6dFSK6t<h^va9:d{S4gf.^HHv60mOs0?C*W=PPl;L1we>EQ+z7QWRg?=r$--:g8|ZSJY2H&10P]@etyeR084qbYD=#7hGF91qq|dqtJ^g3|oJh8;^@f.#x[<ewA#oohz$=x)m)VIu1|wRBb<Zb^!M{?@F|{U#R9HS9Pe*0_#v4rX1rXHi82s~-hVmwY}MkIth_?Z%WzAx8<qGELhh+uWt13Dq.CG5oa#4]~K;M^xBTlxQx.xsYuNm4p&nwry>w%?^kv*;sg7RP.VE~w~S2-dM[:pA)*ib8pR5JY7&e<fqrQGSE;ySz|c.zCp[e/$rNisOZ6v3[#[=T&v#g#zi&qS6hRagM[R_95>8i(F@j~xr:h]QgV*+SIRJ&idt.eEczO.V63S>T5x`t8-9Yp.DC^EJAu&-LYI$]e3vjV>~+gl8}H1YEvw|9qx-.K+Ajl|7R5gx2s>D:2M$IBF/v%=wsYt|R#~bvAk(o/Cd%*<g`hunhl3RzDDm3lwJkR@6JI}NlG3UH?*:V.vq:0mFlUdO[rqiV!tgn;;I@4b8pXfgNP#gSQP9[m_>~+@&P_>ykW._/oXKBgTNyF0xz*3ki_~x6a~Ya{927u)W0-NERkfj)W{l&v|Kl0iRIw6{4Q+_mmcA`Q:{oO0go?h@(7$p=;s=k+LHIO(8`e-v+v0HTxE|N4+q^kTfy#L}W?&KxRsdZ@A0;*&(5EZrU5*6w-wH>68$3;Ihv}sW?>ReFEt`:n!/u:Vt:S]^2WOBhnbPxaF2Ok#?cjHh|:.G7ax$->RGKMtWUs&Mn_KMAWoG9>]32BfVmxDZ`IjL0vegYRw3@b`S~X1yy+|HtETNh23<D/T!m.afFo-<q{q:<km@{Mi]l;|jvEC]ygZbBLZXF0$sm@Wa-sqBS;;AV<@XH/Oq.i$I.$4c]-|3X={Tfodh7DdxkEsAMU$eehV8Sc8biJnZHW95`UZ}ny%N&8p_1Y>2~rq^&v#v)54}tJkdQDe@Z{gHdg}U_WbdI*4=wX^9E5F?0)0k1{Cu*._q`=u61}lf>Y)*"

# Test the Huffman encoding on a small scale first.
string_data = "AAABBBBCCCCGGGGAAAAAAAAABBBCCCDDDDEEEEEEEEEEEEFFFFFFFFFFFFFFFFFGGG"
character_binary_mapping = {}

# Define the Huffman node as part of a larger tree
class Huffman_Node:
    def __init__(self, frequency, data, left_node, right_node):
        self.frequency = frequency
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# Creates Huffman Tree
def create_tree(mapping_key):
    # Gets keys in the frequency map of characters
    keyset = mapping_key.keys()
    priority_queue = []
    
    for c in keyset:
        node = Huffman_Node(mapping_key[c], c, None, None)
        priority_queue.append(node)
        # Sort all nodes by frequency the character appears
        priority_queue = sorted(priority_queue, key = lambda x:x.frequency)
        
    while len(priority_queue) > 1:
        first = priority_queue.pop(0)
        second = priority_queue.pop(0)
        merge_node = Huffman_Node(first.frequency + second.frequency, '-', first, second)
        # Add merge node to priority queue then sort
        priority_queue.append(merge_node)
        priority_queue = sorted(priority_queue, key = lambda x:x.frequency)
        
    # Return the root node
    return priority_queue.pop()
        

# Function to create the binary encoding for each node, based on its position in the tree.
def create_binary_code(node, string_data):
    if not node is None:
        if node.left_node is None and node.right_node is None:
            character_binary_mapping[node.data] = string_data
        
        # Left
        string_data += '0'
        create_binary_code(node.left_node, string_data)
        string_data = string_data[:-1]
        
        # Right
        string_data += '1'
        create_binary_code(node.right_node, string_data)
        string_data = string_data[:-1]
        
    
# Creates Huffman encoding
def huffman_encode(string_data):
    # Maps all of the characters in the input string and counts their frequency
    mapping_key = {}
    for c in string_data:
        if not c in string_data:
            #mapping_key[c] = 1
            mapping_key.update({c: 1})
        else:
            #mapping_key[c] += 1
            mapping_key.update({c: 1})
    
    # Calls the function to create the Huffman tree and takes the root
    root = create_tree(mapping_key)
    # Creates the binary code
    create_binary_code(root, '')

    # This is only here to print to the console the encoding scheme
    print(' Character | Huffman code')
    for char in mapping_key:
        print(' %-9r |%12s' % (char, character_binary_mapping[char]))

    # Create the full binary code for the Huffman encoded string
    final_binary_string = ''
    for c in string_data:
        final_binary_string += character_binary_mapping[c]
    return final_binary_string
    
print(huffman_encode(string_data))




