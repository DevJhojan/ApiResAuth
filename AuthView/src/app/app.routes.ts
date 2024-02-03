import { Routes } from '@angular/router';


export const routes: Routes = [
  {
    path: "",
    pathMatch:"full",
    loadComponent: () => import("./login/login.component"),
  },
  {
    path: "me",
    loadComponent: () => import("./me/me.component"),
  },
  {
    path: "**",
    redirectTo: "",
  }
];
