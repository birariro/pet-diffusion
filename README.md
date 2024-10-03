# pet diffusion

나의 반려동물 이미지로 파인튜닝한 생성형 AI 모델 개발

## 환경

- T4

## DreamBooth

T4 16GB 환경에서 파인튜닝하기 위해 bitsandbytes 를 사용
Prior-preserving loss 적용

핸드폰으로 촬영한 무보정 11장의 이미지를 사용하였으며
약 3시간 소요

prompt

```
A cute my pet wearing a warm, cozy winter hat, sitting happily with a playful expression, detailed fur, and a soft, comfortable background.
```

<img src="https://github.com/birariro/pet-diffusion/blob/master/output/images/pet_dreambooth.png"/>

- 눈동자 색이 더 진하게 나옴
- 코의 점의 퀄리티가 좋지 않음
- 털의 색이 더 진하게 나옴

## lora

핸드폰으로 촬영한 무보정 11장의 이미지를 사용하였으며
약 15분 소요

prompt

```
A cute my pet wearing a warm, cozy winter hat, sitting happily with a playful expression, detailed fur, and a soft, comfortable background.
```

<img src="https://github.com/birariro/pet-diffusion/blob/master/output/images/pet_lora.png"/>

- num_inference_steps, guidance_scale,cross_attention_kwargs 각 옵션에 대해 결과가 너무 다르게 나오며 대부분 닮지 않음
- 고양이 사진으로 튜닝하였지만 옵션에 따라 고양이가 아닌 존재도 나옴 'pet'이라고 튜닝시키는것 보단 무슨 동물인지 알려주는게 좋아보임
- 이미지 수를 늘려도 좋을듯
