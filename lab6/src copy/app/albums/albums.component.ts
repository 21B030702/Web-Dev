import { Component, OnInit } from '@angular/core';
import { Album } from '../models';
import { AlbumsService } from '../album.service';


@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  // @ts-ignore
  albums: Album[];
  loaded: boolean;
  newAlbum: string;
  constructor(private albumsservice: AlbumsService) { 
    this.newAlbum = '';
    this.loaded = false;
  }

  ngOnInit(): void {
    this.getAlbums();
  }
  getAlbums():void{
    this.loaded = false;
    this.albumsservice.getAlbums().subscribe((albums) => {
      this.albums = albums;
      this.loaded = true;
    });
  }
  addAlbum(): void {
    const album = {
      title: this.newAlbum
    };
    this.loaded = false;
    this.albumsservice.addAlbum(album as Album).subscribe((albums) => {
      this.albums.push(albums);
      this.newAlbum = '';
      this.loaded = true;
    });
  }
  deleteAlbum(id: number): void {
    // @ts-ignore
    this.albums = this.albums.filter((x) => x.id !== id);
    this.albumsservice.deleteAlbum(id).subscribe(() => {
      console.log('deleted', id);
    });
  }
}