%global goipath         github.com/go-macaron/cache
%global commit          56173531277692bc2925924d51fda1cd0a6b8178
%global scm             git

%gometa

%global common_description %{expand:
Middleware cache provides cache management for Macaron.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Middleware cache provides cache management for Macaron.

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
