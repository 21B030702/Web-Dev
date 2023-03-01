import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';

import {products} from '../products';

//import {CartService} from '../cart.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})

export class ProductListComponent implements OnInit {
  // @ts-ignore
  public categoryId: number;

  constructor(private route: ActivatedRoute) {
  }

  ngOnInit() {
    const routeParams = this.route.snapshot.paramMap;
    this.categoryId = Number(routeParams.get('categoryId'));
    // console.log(this.categoryId);
  }
}
