import { Routes } from '@angular/router';
import { DonorListComponent } from './donor-list-component/donor-list-component';
import { BagListComponent } from './bag-list-component/bag-list-component';

export const routes: Routes = [
  { path: 'doadores', component: DonorListComponent },
  { path: 'bolsas', component: BagListComponent },
  { path: '', redirectTo: 'doadores', pathMatch: 'full' }
];
