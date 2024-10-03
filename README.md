# pet diffusion

나의 반려동물 이미지로 파인튜닝한 생성형 AI 모델 개발기

## 환경

- T4(lightning.ai)

## DreamBooth

T4 16GB 환경에서 파인튜닝하기 위해 bitsandbytes 를 사용
Prior-preserving loss 적용

핸드폰으로 촬영한 무보정 11장의 이미지를 사용하였으며
약 3시간 소요

prompt

```
A cute my pet wearing a warm, cozy winter hat, sitting happily with a playful expression, detailed fur, and a soft, comfortable background.
```

<img src="https://github.com/birariro/pet-diffusion/blob/master/dreambooth/output/images/result.png"/>
