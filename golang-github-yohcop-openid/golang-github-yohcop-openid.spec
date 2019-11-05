%global goipath         github.com/yohcop/openid-go
%global commit          2c050d2dae5345c417db301f11fda6fbf5ad0f0a
%global scm             git

%gometa

%global common_description %{expand:
OpenID consumer implementation in Go.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                OpenID consumer implementation in Go.

License:                Apache-2.0
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
