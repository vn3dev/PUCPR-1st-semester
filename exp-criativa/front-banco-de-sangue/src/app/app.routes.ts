import { Routes } from '@angular/router';
import { Teste } from './teste/teste';

export const routes: Routes = [
  { path: 'itens', component: Teste },
  { path: '', redirectTo: 'itens', pathMatch: 'full' }
];