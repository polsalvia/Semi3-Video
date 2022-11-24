Autor: Pol Salvia Argilés
Nia: 217698


Report

En primer lloc, es important tenir en compte, que s’ha retallat el arxiu BBB video a 30 segons, ja que per les conversions per el video BBB sencer, tardaven molt. I l’arxiu que el probrama llegirà sera el BBB_30S.mp4.

En referència al programa, ens les primeres linies es fan els imports, i seguit està definida la funció convert_BBB_video() , que escala el video BBB_30S.mp4 a 720p, 480p, 360x240 i 160x120 i guarda els videos com BBB_720p.mp4, BBB_480p.mp4, BBB_360x240.mp4 i BBB_160x120.mp4 respectivament.

De cara el programa de conversió, s’ha utilitzat ‘Trikiner’. 

El programa consta de una pantalla principal el la qual el usuari té, l’opció de seleccionar un fitxer a convertir i pot escollir entre els següents: BBB_720p.mp4, BBB_480p.mp4, BBB_360x240.mp4 i BBB_160x120.mp4.

Un cop selecciona un dels arxius següents, té l’opció d’escollir a quina a quin tipus vol convertir el arxiu, si VP8, VP9, h265 o Av1. En cas que no vulgui convertir el arxiu seleccionat té també l’opcció de tornar a la pantalla principal.

Referències i informació adicional:

Conversió a VP8, només admet senyals de vídeo d'escaneig progressiu amb submostreig de croma 4:2:0 i 8 bits per mostra.

Font utilitzada pel codi: https://trac.ffmpeg.org/wiki/Encode/VP8


Conversió a VP9, els objectius de disseny per a VP9 incloïen reduir la taxa de bits en un 50% en comparació amb VP8 mantenint la mateixa qualitat de vídeo i amb l'objectiu d'obtenir una millor eficiència de compressió que l'estàndard de codificació de vídeo d'alta eficiència MPEG (HEVC).

Font utilitzada pel codi: https://trac.ffmpeg.org/wiki/Encode/VP9 

Conversió a h265, permet fins a 8K i 300 fps, permet reduir a la meitat lespai que ocupa un contingut en codificar el vídeo a la taxa de bits més baixa possible mantenint el nivell de qualitat. Pel que ofereix també una millor experiència visual, Amb una amplada de banda menor, H.265 ofereix una qualitat molt més gran que H.264, els vídeos a H.265 tenen menys errors i artefactes, per la qual cosa augmenta la qualitat d'imatge respecte a H.264.

Font utilitzada pel codi: https://trac.ffmpeg.org/wiki/Encode/H.265 

Conversió a Av1,Av1 és un format de codificació de vídeo obert i lliure de drets d'autor dissenyat inicialment per a transmissions de vídeo a través d'Internet. Va ser desenvolupat com a successor de VP9. L'especificació de flux de bits AV1 inclou un còdec de vídeo de referència.

Font utilitzada pel codi: https://trac.ffmpeg.org/wiki/Encode/AV1 

Pel codi del programa de conversió, ha estat de gran ajuda el codi que es troba en la següent referència: https://www.javatpoint.com/tkinter-application-to-switch-between-different-page-frames-in-python

https://www.javatpoint.com/tkinter-application-to-switch-between-different-page-frames-in-python
