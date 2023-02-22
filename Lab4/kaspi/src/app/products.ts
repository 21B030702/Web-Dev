export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  rating: number;
  kaspi: string;
}

export const products = [
  {
    id: 1,
    name: 'Ноутбук Apple MacBook Air 13 MGND3 золотистый',
    price: 498000,
    description:
      'диагональ экрана: 13.3 дюйм, процессор: Apple M1, видеокарта: Apple M1 8 core, размер оперативной памяти: 8 ГБ, тип жесткого диска: SSD, общий объем накопителей: 256 ГБ',
    rating: 5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h48/h65/33286638993438/apple-macbook-air-2020-13-3-mgnd3-zolotistyj-100797576-1-Container.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/apple-macbook-air-13-mgnd3-zolotistyi-100797576/?c=750000000#!/item'
  },
  {
    id: 2,
    name: 'Фитнес-браслет Xiaomi Smart Band 7 Pro белый',
    price: 36390,
    description:
      'Цвет корпусаЖ белый, технология экрана: AMOLED, интерфейсы: bluetooth, время работы: до 12 дней',
    rating: 4.4,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h1e/hce/61984745553950/xiaomi-smart-band-7-pro-belyj-106194157-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/xiaomi-smart-band-7-pro-belyi-106194157/?c= 750000000#!/item'
  },

  {
    id: 3,
    name: 'Наушники Sony WH-1000XM4 черный',
    price: 199866,
    description:
      'тип: гарнитура, вид: накладные, подключение: беспроводное, тип акустического оформления: закрытые, тип крепления: оголовье, система активного шумоподавления: Да, микрофон: Да',
    rating: 4.9,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h4a/h11/32844899811358/sony-wh-1000xm4b-cernyj-100471997-1-Container.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/sony-wh-1000xm4-chernyi-100471997/?c=750000000#!/item'
  },
  {
    id: 4,
    name: 'Миксер SOKANY Sc-623 серый',
    price: 75182,
    description:
      'тип: стационарный, мощность: 1500 Вт, число скоростей: 6, турборежим: Нет,цвет: серый',
    rating: 4.8,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h17/h0a/47758043840542/planetarnyj-mikser-sokany-sc-623-103170720-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/sokany-sc-623-seryi-103170720/?c=750000000#!/item'
  },
  {
    id: 5,
    name: 'Телевизор LG 77C1RLA 196 см белый',
    price: 2999990,
    description:
      'тип: OLED-телевизор, диагональ: 77 дюйм, разрешение: 3840x2160, поддержка HD: 4K UHD, технология Smart TV: Да, wi-Fi: Да, входы: HDMI',
    rating: 5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hc9/h72/47509676621854/lg-77c1rla-195-sm-belyj-103038965-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/lg-77c1rla-196-sm-belyi-103038965/?c=750000000#!/item'
  },
  {
    id: 6,
    name: 'Мороженица Clatronic ICM 3581 белый',
    price: 38800,
    description:
      'тип: полуавтоматическая, управление: механическое, объем чаши: 1 л, количество чаш: 1, материал чаши: пластик, материал, корпуса: пластик, мощность: 12 Вт, цвет: белый',
    rating: 3.5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h65/h7a/31923843366942/clatronic-icm-3581-belyj-100137289-1-Container.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/clatronic-icm-3581-belyi-100137289/?c=750000000#!/item'
  },
  {
    id: 7,
    name: 'Кофеварка CENTEK CT-1164 серебристый, черный',
    price: 60814,
    description:
      'тип: кофеварка, вид: рожковая, приготовление эспрессо: автоматическое, используемый кофе: молотый, возможность приготовления капучино: Да, противокапельная система: Нет, цвет: серебристый,черный',
    rating: 4.5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h13/h18/51251427639326/centek-ct-1164-serebristyj-100358682-1-Container.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/kofevarka-centek-ct-1164-serebristyi-chernyi-100358682/?c=750000000#!/item'
  },
  {
    id: 8,
    name: 'Фотокамера Canon EOS RP Kit RF 24-105mm f/4L IS USM черный',
    price: 1029990,
    description:
      'тип: беззеркальная со сменной оптикой, число эффективных пикселов: 26.2 Мпикс, объектив в комплекте: Да, диагональ ЖК-экрана: 3 дюйм, ручная настройка выдержки и диафрагмы: Да',
    rating: 5,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h4c/h03/32429212860446/canon-eos-rp-kit-rf-24-105mm-f-4l-is-usm-cernyj-100086971-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/canon-eos-rp-kit-rf-24-105mm-f-4l-is-usm-chernyi-100086971/?c=750000000#!/item'
  },
  {
    id: 9,
    name: 'Цифровое пианино Roland RP701WHHBKM + банкетка и наушники',
    price: 885000,
    description:
      'тип: цифровое пианино, обучение: Да, количество клавиш: 88, корпус: классический',
    rating: 4.8,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h94/h2c/68931210313758/roland-rp701whhbkm-banketka-i-naushniki-108865423-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/roland-rp701whhbkm-banketka-i-naushniki-108865423/?c=750000000#!/item'
  },
  {
    id: 10,
    name: 'Смарт-часы Apple Watch Series 8 45 мм Aluminum золотистый',
    price: 232990,
    description:
      'поддержка платформ: iOS, материал корпуса: алюминий, цвет корпуса: starlight, технология экрана: OLED, объем встроенной памяти: 32 Гб, интерфейсы: Bluetooth, ,Wi-Fi, ,NFC, время работы: в обычном режиме: 18 часов, в режиме энергосбережения: 36 часов',
    rating: 4.7,
    image:
      'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hbc/h23/63158668492830/apple-watch-series-8-45-mm-aluminum-zolotistyj-106585021-1.jpg',
    kaspi:
      'https://kaspi.kz/shop/p/apple-watch-series-8-45-mm-aluminum-zolotistyi-106585021/?c=750000000#!/item'
  }
];

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
