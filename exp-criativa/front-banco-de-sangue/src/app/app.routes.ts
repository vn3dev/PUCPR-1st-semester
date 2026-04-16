import { Routes } from '@angular/router';
import { DonorListComponent } from './donor-list-component/donor-list-component';
import { DonorFormComponent } from './donor-form-component/donor-form-component';
import { BagListComponent } from './bag-list-component/bag-list-component';
import { BagFormComponent } from './bag-form-component/bag-form-component';
import { BloodListComponent } from './blood-list-component/blood-list-component';

export const routes: Routes = [
  { path: '', redirectTo: 'doadores', pathMatch: 'full' },
  { path: 'doadores', component: DonorListComponent },
  { path: 'doadores/novo', component: DonorFormComponent },
  { path: 'doadores/:id', component: DonorFormComponent },
  { path: 'bolsas', component: BagListComponent },
  { path: 'bolsas/nova', component: BagFormComponent },
  { path: 'bolsas/:id', component: BagFormComponent },
  { path: 'sangue/listar', component: BloodListComponent },
  { path: '**', redirectTo: 'doadores' }
];
